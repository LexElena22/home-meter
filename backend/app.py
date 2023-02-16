from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import mls_info_provider
import scoring_provider
import validator

# ------------------------APP--------------------------------------------

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{host}:{port}/{database}'.format(
    username='postgres',
    password='[PASSWORD]',
    host='flask-dbinstance.cihltfddjxu1.us-west-2.rds.amazonaws.com',
    port='5432',
    database='homemeter_development',
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "somethinguniqßue"

db = SQLAlchemy(app)

CORS(app)

# ______________________TESTING______________________________

# @app.route('/', methods=['GET'])
# def get_data():
#     init_logger()
#     conn = psql_connection()
#     create_table(conn)
#     load(conn)
#     logging.info("End of program.")

#     return ""

# ------------------------ROUTES------------------------------------------

from models.PropertyGeneral import PropertyGeneral


# GET all
@app.route('/', methods=['GET'])
def get_all_properties():
    properties = PropertyGeneral.query.all()

    result = []
    for item in properties:
        result.append(item.to_dict())

    return jsonify(result), 200


@app.route('/findproperty/<mls_query>', methods=['GET'])
def get_property_data(mls_query):
    if not mls_query:
        return {"message": "Must provide an mls id"}

    valid_mls = validator.validate_mls(mls_query)

    if valid_mls is None:
        return {"message": "Invalids mls id"}

    property_from_db = PropertyGeneral.query.filter_by(mls_id=valid_mls).first()

    if not property_from_db:
        property_json_from_api = mls_info_provider.get_property_as_json(valid_mls)
        if property_json_from_api is None:
            return {"message": "Mls Not Found"}
        property_obj = PropertyGeneral(property_json_from_api)
        # insert into DB
        db.session.add(property_obj)
        db.session.commit()

        property_from_db = PropertyGeneral.query.filter_by(mls_id=valid_mls).first()

    scoring_options = scoring_provider.find_scoring_options(property_from_db)

    return jsonify(scoring_options)

@app.route('/score/<mls>', methods=['POST'])
def get_score_data(mls):
    categories = request.get_json()

    if categories is None or len(categories) == 0:
        return {"message": "Invalids Categories"}

    property_general = PropertyGeneral.query.filter_by(mls_id=mls).first()
    scoring_result = scoring_provider.score_property(property_general, categories)

    return scoring_result

# ------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
