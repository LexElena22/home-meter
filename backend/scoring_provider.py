SCHOOL = "Near Schools"
SQFT = "Sqft"
HOA = "Low HOA"
NOISE = "Low Noise Level"
ONE_STORY = "One Story"
YEAR = "Newer Home"
PARKING = "Garage or Reserved Parking"
HEATING_COOLING = "Heating and Cooling"
MONTHLY_PAYMENT = "Monthly Payment"
VIEW = "Has View"
REMODELED = "Recently Remodeled"
PET_FRIENDLY = "Pet Friendly"
PUBLIC_TRANS = "Public Transportation"
BACKYARD = "Back Yard"
AMENITIES = "Amenities and Community Features"


def find_scoring_options(property_general):
    options = []
    options.append(SCHOOL)
    options.append(HOA)
    options.append(NOISE)
    options.append(ONE_STORY)
    options.append(REMODELED)
    if property_general.sqft and property_general.sqft > 0:
        options.append(SQFT)
    if property_general.year_built and property_general.year_built > 0:
        options.append(YEAR)
    if property_general.has_parking_info():
        options.append(PARKING)
    if property_general.has_heating_cooling_info():
        options.append(HEATING_COOLING)
    if "mortgage" in property_general.property_detail and "estimate" in property_general.property_detail["mortgage"]:
        options.append(MONTHLY_PAYMENT)
    if property_general.has_view_info():
        options.append(VIEW)
    if property_general.has_amenities_info():
        options.append(AMENITIES)
    # options.append(PET_FRIENDLY)
    # options.append(PUBLIC_TRANS)
    # options.append(BACKYARD)

    return options


def __scoresqft(property_general, total_points, priority, descriptions_list):
    sqft = property_general.sqft
    if priority == 1:
        if sqft < 500:
            total_points -= 70
        elif sqft < 1000:
            total_points -= 50
        elif sqft < 1200:
            total_points -= 45
        elif sqft < 1500:
            total_points -= 40
        elif sqft < 1800:
            total_points -= 30
        elif sqft < 2000:
            total_points -= 20
        elif sqft < 3000:
            total_points -= 10
        elif sqft < 3000:
            total_points -= 5
    elif priority == 2:
        if sqft < 500:
            total_points -= 50
        elif sqft < 1000:
            total_points -= 40
        elif sqft < 1200:
            total_points -= 30
        elif sqft < 1500:
            total_points -= 20
        elif sqft < 1800:
            total_points -= 10
        elif sqft < 2000:
            total_points -= 5
        elif sqft < 3000:
            total_points -= 3
    elif priority == 3:
        if sqft < 500:
            total_points -= 40
        elif sqft < 1000:
            total_points -= 30
        elif sqft < 1200:
            total_points -= 20
        elif sqft < 1500:
            total_points -= 10
        elif sqft < 1800:
            total_points -= 5
        elif sqft < 2000:
            total_points -= 3

    descriptions_list.append(f'SQFT: {"{:,}".format(sqft)} sqft')
    return total_points


def __scoreschool(property_general, total_points, priority, descriptions_list):
    schools = property_general.property_detail["schools"]
    if priority == 1:
        if schools is None or len(schools) == 0:
            total_points -= 70
        elif len(schools) < 2:
            total_points -= 50
        elif len(schools) < 4:
            total_points -= 40
        elif len(schools) < 5:
            total_points -= 25
        elif len(schools) < 6:
            total_points -= 20
        elif len(schools) < 7:
            total_points -= 10
        elif len(schools) < 8:
            total_points -= 5
        elif len(schools) <= 9:
            total_points -= 2
    elif priority == 2:
        if schools is None or len(schools) == 0:
            total_points -= 50
        elif len(schools) < 2:
            total_points -= 40
        elif len(schools) < 4:
            total_points -= 30
        elif len(schools) < 5:
            total_points -= 20
        elif len(schools) < 6:
            total_points -= 10
        elif len(schools) < 7:
            total_points -= 3
    elif priority == 3:
        if schools is None or len(schools) == 0:
            total_points -= 40
        elif len(schools) < 2:
            total_points -= 30
        elif len(schools) < 4:
            total_points -= 20
        elif len(schools) < 5:
            total_points -= 5
        elif len(schools) < 6:
            total_points -= 2

    descriptions_list.append(f'Schools: found {"{:,}".format(len(schools))} schools nearby')
    return total_points


def __scorehoa(property_general, total_points, priority, descriptions_list):
    hoa_fee = property_general.property_detail["hoa_fee"]
    if hoa_fee is None or hoa_fee == "0" or hoa_fee == 0:
        descriptions_list.append(f'HOA: No HOA')
        return total_points

    hoa_fee = int(hoa_fee)

    if priority == 1:
        if hoa_fee > 5000:
            total_points -= 75
        elif hoa_fee > 4500:
            total_points -= 70
        elif hoa_fee > 4000:
            total_points -= 60
        elif hoa_fee > 3000:
            total_points -= 55
        elif hoa_fee > 2000:
            total_points -= 50
        elif hoa_fee > 1500:
            total_points -= 45
        elif hoa_fee > 1000:
            total_points -= 40
        elif hoa_fee > 700:
            total_points -= 35
        elif hoa_fee > 500:
            total_points -= 30
        elif hoa_fee > 300:
            total_points -= 25
        elif hoa_fee > 250:
            total_points -= 20
        elif hoa_fee > 200:
            total_points -= 10
        elif hoa_fee > 100:
            total_points -= 5
        elif hoa_fee > 50:
            total_points -= 2
        elif hoa_fee > 10:
            total_points -= 1
    elif priority == 2:
        if hoa_fee > 5000:
            total_points -= 70
        elif hoa_fee > 4500:
            total_points -= 65
        elif hoa_fee > 4000:
            total_points -= 60
        elif hoa_fee > 3000:
            total_points -= 55
        elif hoa_fee > 2000:
            total_points -= 50
        elif hoa_fee > 1500:
            total_points -= 40
        elif hoa_fee > 1000:
            total_points -= 30
        elif hoa_fee > 700:
            total_points -= 25
        elif hoa_fee > 500:
            total_points -= 20
        elif hoa_fee > 300:
            total_points -= 15
        elif hoa_fee > 250:
            total_points -= 10
        elif hoa_fee > 200:
            total_points -= 5
        elif hoa_fee > 100:
            total_points -= 2
    elif priority == 3:
        if hoa_fee > 5000:
            total_points -= 50
        elif hoa_fee > 4500:
            total_points -= 45
        elif hoa_fee > 4000:
            total_points -= 40
        elif hoa_fee > 3000:
            total_points -= 35
        elif hoa_fee > 2000:
            total_points -= 30
        elif hoa_fee > 1500:
            total_points -= 25
        elif hoa_fee > 1000:
            total_points -= 20
        elif hoa_fee > 700:
            total_points -= 15
        elif hoa_fee > 500:
            total_points -= 10
        elif hoa_fee > 300:
            total_points -= 5
        elif hoa_fee > 200:
            total_points -= 3
        elif hoa_fee > 100:
            total_points -= 1

    descriptions_list.append(f'HOA: found ${"{:,}".format(hoa_fee)} monthly HOA fees')
    return total_points


def __scorenoise(property_general, total_points, priority, descriptions_list):
    noise = property_general.property_detail["noise"]

    if noise is None or len(noise) == 0:
        print("Missing noise info")
        return total_points

    noise_score = int(noise["score"])

    # print(f"score: {noise_score} priority: {priority}")
    if priority == 1:
        total_points -= noise_score
    elif priority == 2:
        total_points -= (noise_score - 20)
    elif priority == 3:
        total_points -= (noise_score - 40)

    descriptions_list.append(f'Noise: a noise of level {noise["score_text"]}')
    return total_points


def __scoreonestory(property_general, total_points, priority, descriptions_list):
    stories = property_general.property_detail["stories"]

    if stories is None and "public_records" in property_general.property_detail:
        public_records = property_general.property_detail["public_records"]

        if public_records is not None and len(public_records) > 0:
            stories = public_records[0]["stories"]

    if stories is None:
        return total_points

    stories = int(stories)
    # print(f"stories: {stories}")

    if priority == 1:
        if stories >= 5:
            total_points -= 75
        elif stories >= 4:
            total_points -= 70
        elif stories >= 3:
            total_points -= 65
        elif stories >= 2:
            total_points -= 50
    elif priority == 2:
        if stories >= 5:
            total_points -= 65
        elif stories >= 4:
            total_points -= 60
        elif stories >= 3:
            total_points -= 55
        elif stories >= 2:
            total_points -= 30
    elif priority == 3:
        if stories >= 5:
            total_points -= 60
        elif stories >= 4:
            total_points -= 55
        elif stories >= 3:
            total_points -= 40
        elif stories >= 2:
            total_points -= 20

    descriptions_list.append(f'One Story: {stories} stories')
    return total_points


def __scoreyear(property_general, total_points, priority, descriptions_list):
    year = property_general.year_built

    if priority == 1:
        if year >= 2022:
            total_points -= 0
        elif year >= 2018:
            total_points -= 3
        elif year >= 2015:
            total_points -= 5
        elif year >= 2010:
            total_points -= 15
        elif year >= 2000:
            total_points -= 20
        elif year >= 1990:
            total_points -= 30
        elif year >= 1980:
            total_points -= 45
        elif year >= 1970:
            total_points -= 55
        elif year >= 1950:
            total_points -= 65
        elif year >= 1940:
            total_points -= 75
        elif year >= 1920:
            total_points -= 85
        elif year >= 1900:
            total_points -= 95
        else:
            total_points -= 98
    elif priority == 2:
        if year >= 2022:
            total_points -= 0
        elif year >= 2018:
            total_points -= 2
        elif year >= 2015:
            total_points -= 3
        elif year >= 2010:
            total_points -= 10
        elif year >= 2000:
            total_points -= 15
        elif year >= 1990:
            total_points -= 20
        elif year >= 1980:
            total_points -= 35
        elif year >= 1970:
            total_points -= 45
        elif year >= 1950:
            total_points -= 55
        elif year >= 1940:
            total_points -= 65
        elif year >= 1920:
            total_points -= 70
        elif year >= 1900:
            total_points -= 85
        else:
            total_points -= 90
    elif priority == 3:
        if year >= 2018:
            total_points -= 0
        elif year >= 2010:
            total_points -= 3
        elif year >= 2000:
            total_points -= 10
        elif year >= 1990:
            total_points -= 15
        elif year >= 1980:
            total_points -= 20
        elif year >= 1970:
            total_points -= 30
        elif year >= 1950:
            total_points -= 40
        elif year >= 1940:
            total_points -= 50
        elif year >= 1920:
            total_points -= 60
        elif year >= 1900:
            total_points -= 70
        else:
            total_points -= 80

    descriptions_list.append(f'Year Built: {year}')
    return total_points


def __scoreparking(property_general, total_points, priority, descriptions_list):
    parking_info = property_general.parking_info()
    if parking_info is None:
        return total_points

    parking_cnt = 0
    description = ""
    for text in parking_info:
        if "Spaces:" in text:
            parking_cnt = int(text[-1])
        elif "Features: " in text:
            description = text.split("Features: ", 1)[1]

    # print(f"space: {parking_cnt}, description: {description}")

    if priority == 1:
        if parking_cnt >= 3:
            total_points -= 0
        elif parking_cnt >= 2:
            total_points -= 2
        elif parking_cnt >= 1:
            total_points -= 5
        else:
            if "Street" in description:
                total_points -= 50
            elif "No Garage" in description:
                total_points -= 70
            else:
                total_points -= 60
    elif priority == 2:
        if parking_cnt >= 3:
            total_points -= 0
        elif parking_cnt >= 2:
            total_points -= 1
        elif parking_cnt >= 1:
            total_points -= 3
        else:
            if "Street" in description:
                total_points -= 30
            elif "No Garage" in description:
                total_points -= 60
            else:
                total_points -= 40
    elif priority == 3:
        if parking_cnt >= 2:
            total_points -= 0
        elif parking_cnt >= 1:
            total_points -= 1
        else:
            if "Street" in description:
                total_points -= 20
            elif "No Garage" in description:
                total_points -= 50
            else:
                total_points -= 30

    descriptions_list.append(f'Parking or Garage: {", ".join(parking_info)}')
    return total_points


def __scoreheatingcooling(property_general, total_points, priority, descriptions_list):
    features = property_general.heating_cooling_info()
    features_cnt = len(features)

    if priority == 1:
        if features_cnt == 0:
            total_points -= 75
        elif features_cnt == 1:
            total_points -= 40
        elif features_cnt == 2:
            total_points -= 20
        elif features_cnt < 4:
            total_points -= 10
    elif priority == 2:
        if features_cnt == 0:
            total_points -= 60
        elif features_cnt == 1:
            total_points -= 30
        elif features_cnt == 2:
            total_points -= 10
        elif features_cnt < 4:
            total_points -= 2
    elif priority == 3:
        if features_cnt == 0:
            total_points -= 50
        elif features_cnt == 1:
            total_points -= 20
        elif features_cnt == 2:
            total_points -= 5

    if features_cnt > 0:
        descriptions_list.extend(features)
    else:
        descriptions_list.append("No Heating or Cooling")

    descriptions_list.append(f'Heating or Cooling: {", ".join(features)}')
    return total_points


def __scoremonthlypayment(property_general, total_points, priority, descriptions_list):
    estimates = property_general.property_detail["mortgage"]["estimate"]
    monthly_payment = int(estimates["monthly_payment"])

    if priority == 1:
        if monthly_payment > 10000:
            total_points -= 70
        elif monthly_payment > 8000:
            total_points -= 60
        elif monthly_payment > 5000:
            total_points -= 50
        elif monthly_payment > 4000:
            total_points -= 40
        elif monthly_payment > 3000:
            total_points -= 35
        elif monthly_payment > 2500:
            total_points -= 30
        elif monthly_payment > 2000:
            total_points -= 20
        elif monthly_payment > 1500:
            total_points -= 10
        elif monthly_payment > 1000:
            total_points -= 5
        elif monthly_payment > 800:
            total_points -= 3
    elif priority == 2:
        if monthly_payment > 10000:
            total_points -= 60
        elif monthly_payment > 8000:
            total_points -= 50
        elif monthly_payment > 5000:
            total_points -= 40
        elif monthly_payment > 4000:
            total_points -= 30
        elif monthly_payment > 3000:
            total_points -= 25
        elif monthly_payment > 2500:
            total_points -= 20
        elif monthly_payment > 2000:
            total_points -= 15
        elif monthly_payment > 1500:
            total_points -= 5
        elif monthly_payment > 1000:
            total_points -= 3
        elif monthly_payment > 800:
            total_points -= 2
    elif priority == 3:
        if monthly_payment > 10000:
            total_points -= 50
        elif monthly_payment > 8000:
            total_points -= 40
        elif monthly_payment > 5000:
            total_points -= 30
        elif monthly_payment > 4000:
            total_points -= 25
        elif monthly_payment > 3000:
            total_points -= 20
        elif monthly_payment > 2500:
            total_points -= 15
        elif monthly_payment > 2000:
            total_points -= 10
        elif monthly_payment > 1500:
            total_points -= 3
        elif monthly_payment > 1000:
            total_points -= 2
        elif monthly_payment > 800:
            total_points -= 1

    descriptions_list.append(
        f'Estimate monthly payment of ${"{:,}".format(monthly_payment)}, this is an estimate based on an average interest rate and includes mortgage, ${"{:,}".format(estimates["monthly_property_taxes"])} monthly property taxes, ${"{:,}".format(estimates["monthly_home_insurance"])} monthly home insurance')

    return total_points


def __scoreview(property_general, total_points, priority, descriptions_list):
    view_info = property_general.view_info()
    if view_info is None:
        return total_points

    view_cnt = 0
    description = ""
    for text in view_info:
        if "View: " in text:
            description = text
            view_cnt = len((text.split("View: ", 1)[1]).split(","))

    if priority == 1:
        if view_cnt < 1:
            total_points -= 75
        elif view_cnt < 2:
            total_points -= 50
        elif view_cnt < 3:
            total_points -= 40
        elif view_cnt < 4:
            total_points -= 18
    elif priority == 2:
        if view_cnt < 1:
            total_points -= 60
        elif view_cnt < 2:
            total_points -= 40
        elif view_cnt < 3:
            total_points -= 20
        elif view_cnt < 4:
            total_points -= 5
    elif priority == 3:
        if view_cnt < 1:
            total_points -= 40
        elif view_cnt < 2:
            total_points -= 25
        elif view_cnt < 3:
            total_points -= 5
        elif view_cnt < 4:
            total_points -= 2

    descriptions_list.append(description)
    return total_points


def __scoreremodeled(property_general, total_points, priority, descriptions_list):
    if not property_general.is_remodeled():
        descriptions_list.append("Remodeled")
        if priority == 1:
            total_points -= (2023 - property_general.year_built)
        elif priority == 2:
            total_points -= 20
        elif priority == 3:
            total_points -= 10
    return total_points


def __scoreamenities(property_general, total_points, priority, descriptions_list):
    amenities_info = property_general.amenities_info()
    if amenities_info is None:
        return total_points

    amenities_cnt = 0
    description = ""
    for text in amenities_info:
        if "Community Features: " in text:
            description = text
            amenities_cnt = len((text.split("Community Features: ", 1)[1]).split(","))

    if priority == 1:
        if amenities_cnt < 1:
            total_points -= 75
        elif amenities_cnt < 2:
            total_points -= 50
        elif amenities_cnt < 3:
            total_points -= 40
        elif amenities_cnt < 4:
            total_points -= 18
        elif amenities_cnt < 5:
            total_points -= 5
    elif priority == 2:
        if amenities_cnt < 1:
            total_points -= 60
        elif amenities_cnt < 2:
            total_points -= 40
        elif amenities_cnt < 3:
            total_points -= 20
        elif amenities_cnt < 4:
            total_points -= 5
    elif priority == 3:
        if amenities_cnt < 1:
            total_points -= 40
        elif amenities_cnt < 2:
            total_points -= 25
        elif amenities_cnt < 3:
            total_points -= 5
        elif amenities_cnt < 4:
            total_points -= 2

    descriptions_list.append(description)
    return total_points


# disabled
def __scorepublictrans(property_general, total_points, priority, descriptions_list):
    return total_points


# disabled
def __scorepetfriendly(property_general, total_points, priority, descriptions_list):
    return total_points


# disabled
def __scorebackyard(property_general, total_points, priority, descriptions_list):
    return total_points


def score_property(property_general, categories):
    total_points = len(categories) * 100
    descriptions_list = []
    for category, priority in categories.items():
        if category == SCHOOL:
            total_points = __scoreschool(property_general, total_points, priority, descriptions_list)
        elif category == SQFT:
            total_points = __scoresqft(property_general, total_points, priority, descriptions_list)
        elif category == HOA:
            total_points = __scorehoa(property_general, total_points, priority, descriptions_list)
        elif category == NOISE:
            total_points = __scorenoise(property_general, total_points, priority, descriptions_list)
        elif category == ONE_STORY:
            total_points = __scoreonestory(property_general, total_points, priority, descriptions_list)
        elif category == YEAR:
            total_points = __scoreyear(property_general, total_points, priority, descriptions_list)
        elif category == PARKING:
            total_points = __scoreparking(property_general, total_points, priority, descriptions_list)
        elif category == HEATING_COOLING:
            total_points = __scoreheatingcooling(property_general, total_points, priority, descriptions_list)
        elif category == MONTHLY_PAYMENT:
            total_points = __scoremonthlypayment(property_general, total_points, priority, descriptions_list)
        elif category == VIEW:
            total_points = __scoreview(property_general, total_points, priority, descriptions_list)
        elif category == REMODELED:
            total_points = __scoreremodeled(property_general, total_points, priority, descriptions_list)
        elif category == PET_FRIENDLY:
            total_points = __scorepetfriendly(property_general, total_points, priority, descriptions_list)
        elif category == PUBLIC_TRANS:
            total_points = __scorepublictrans(property_general, total_points, priority, descriptions_list)
        elif category == BACKYARD:
            total_points = __scorebackyard(property_general, total_points, priority, descriptions_list)
        elif category == AMENITIES:
            total_points = __scoreamenities(property_general, total_points, priority, descriptions_list)

    score = total_points / len(categories)

    img = ""
    name = ""
    address = ""
    score_string = ""
    score_string_prefix = "a"

    if property_general.mls_data is not None and property_general.mls_data["primary_photo"] is not None:
        if property_general.mls_data["primary_photo"]["href"] is not None:
            img = property_general.mls_data["primary_photo"]["href"]

    if property_general.address is not None and property_general.address["line"] is not None:
        name = property_general.address["line"]
        address = f'{property_general.address["line"]}, {property_general.address["city"]}, {property_general.address["state"]}, {property_general.address["postal_code"]}'

    if score >= 75:
        score_string = "excellent"
        score_string_prefix = "an"
    elif score >= 50:
        score_string = "good"
    elif score >= 25:
        score_string = "ok"
    elif score >= 0:
        score_string = "bad"

    final_description = f"This home looks to be {score_string_prefix} {score_string} match! It offers: <ul>"
    for description in descriptions_list:
        final_description += "<li>" + description + "</li>"
    final_description += "</ul>"

    return {"score": round(score), "img": img, "name": name, "address": address, "zip": property_general.address["postal_code"], "description": final_description,
            "score_string": score_string}
