# helper class to validate any property information

def validate_mls(mls_input):
    # check if it's valid mls
    # return None if not valid

    mls_input = mls_input.strip()

    if mls_input.isdigit():
        return mls_input

    return None


