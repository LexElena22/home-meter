import requests


# return the property from external API as key,value pairs
def get_property_as_json(mls_query):
    if not mls_query:
        return None
    
    mls_api_response = __find_mls_from_usrealestate_api(mls_query)['data']['results']

    if not mls_api_response or len(mls_api_response) == 0:
        return None

    mls_data = mls_api_response[0]
    property_details_data = __find_property_from_usrealestate_api(mls_data['property_id'])['data']['property_detail']

    return __format_json_data(mls_query, mls_data, property_details_data)

def __format_json_data(mls_id, mls_data, details_data):
    return {
        'mls_id': mls_id,
        'sqft': mls_data['description']['sqft'],
        'year_built': mls_data['description']['year_built'],
        'bedrooms': mls_data['description']['beds'],
        'bathrooms': mls_data['description']['baths'],
        'listed_price': mls_data['list_price'],
        'address': details_data['address'],
        'mls_data': mls_data,
        'property_detail': details_data,
    }

def __find_mls_from_usrealestate_api(mls_id):
    url = "https://us-real-estate.p.rapidapi.com/property-by-mls-id"

    headers = {
    "X-RapidAPI-Key": "KEY",
    "X-RapidAPI-Host": "us-real-estate.p.rapidapi.com"
    }

    return (requests.get(url, headers=headers, params={"mls_id": mls_id}).json())

def __find_property_from_usrealestate_api(property_id):
    url = "https://us-real-estate.p.rapidapi.com/v2/property-detail"

    headers = {
    "X-RapidAPI-Key": "KEY",
    "X-RapidAPI-Host": "us-real-estate.p.rapidapi.com"
    }

    return (requests.get(url, headers=headers, params={"property_id": property_id}).json())