from app import db
from sqlalchemy.dialects.postgresql import JSONB

class PropertyGeneral(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mls_id = db.Column(db.Integer, nullable=False)
    sqft = db.Column(db.Integer)
    year_built = db.Column(db.Integer)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    listed_price = db.Column(db.Integer)
    address = db.Column(JSONB)
    property_detail = db.Column(JSONB)
    mls_data = db.Column(JSONB)

    def to_dict(self):
        return {
            "id": self.id,
            "mls_id": self.mls_id,
            "sqft": self.sqft,
            "year_built": self.year_built,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "listed_price": self.listed_price,
            "address": self.address,
            "mls_data": self.mls_data,
            "property_detail": self.property_detail,
        }

    def is_remodeled(self):
        if self.property_detail["features"] is None:
            return False
        features = self.property_detail["features"]

        for feature in features:
            if feature["category"] == "Building and Construction":
                if "text" in feature and len(feature["text"]) > 0:
                    for item in feature["text"]:
                        if "Remodeled" in item:
                            return True

        return False

    def has_parking_info(self):
        if self.property_detail["features"] is None:
            return False
        features = self.property_detail["features"]

        for feature in features:
            if feature["category"] == "Garage and Parking":
                return True

        return False

    def parking_info(self):
        if self.property_detail["features"] is None:
            return None
        features = self.property_detail["features"]

        for feature in features:
            if feature["category"] == "Garage and Parking":
                if "text" in feature:
                    return feature["text"]
        return None

    def has_amenities_info(self):
        if self.property_detail["features"] is None:
            return False
        features = self.property_detail["features"]

        for feature in features:
            if feature["category"] == "Amenities and Community Features":
                return True

        return False

    def amenities_info(self):
        if self.property_detail["features"] is None:
            return None
        features = self.property_detail["features"]

        for feature in features:
            if feature["category"] == "Amenities and Community Features":
                if "text" in feature:
                    return feature["text"]
        return None

    def has_view_info(self):
        if self.property_detail["features"] is None:
            return False
        features = self.property_detail["features"]

        for feature in features:
            if feature["category"] == "Home Features":
                return True

        return False

    def view_info(self):
        if self.property_detail["features"] is None:
            return None
        features = self.property_detail["features"]

        for feature in features:
            if feature["category"] == "Home Features":
                if "text" in feature:
                    return feature["text"]
        return None

    def has_heating_cooling_info(self):
        if self.property_detail["features"] is None:
            return False
        features = self.property_detail["features"]

        for feature in features:
            if feature["category"] == "Heating and Cooling":
                return True

        return False

    def heating_cooling_info(self):
        if self.property_detail["features"] is None:
            return None
        features = self.property_detail["features"]

        result = []
        for feature in features:
            if feature["category"] == "Heating and Cooling":
                if "text" in feature and len(feature["text"]) > 0:
                    for item in feature["text"]:
                        if "Water Heaters" not in item:
                            result.append(item)
        return result

    def __init__(self, dict):
        if "id" in dict:
            self.id = dict["id"]
        self.mls_id = dict["mls_id"]
        self.sqft = dict["sqft"]
        self.year_built = dict["year_built"]
        self.bedrooms = dict["bedrooms"]
        self.bathrooms = dict["bathrooms"]
        self.listed_price = dict["listed_price"]
        self.address = dict["address"]
        self.property_detail = dict["property_detail"]
        self.mls_data = dict["mls_data"]