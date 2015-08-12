import json
def return_json_from_request_object(data, key):
    """Return json from the ImmutableMultiDict werkzeug gives us

    Convert the incoming data object of type ImmutableMultiDict to a dictionary, look up the value by
    the specified key argument, and convert the response to JSON for a data-interchange format.

    For Jumper, this should be a list of dictionaries at this point, represented in JSON to avoid having to do
    abstract syntax trees to determine if the string is a valid dict.
    """
    data = data.to_dict().get(key)
    data = json.loads(data)
    return data


def return_tuple_from_key_value(data):
    swap = []

    for location in data:

        _tup = list(location.items())[0]
        _lat_long = (_tup[1].split(";"))

        # convert string-type floats to float-type
        _lat_long = float(_lat_long[0]), float(_lat_long[1])
        location = (_tup[0], _lat_long)

        swap.append(location)

    return swap


def req_to_tuple(data, json_key="json"):
    return return_tuple_from_key_value(
        return_json_from_request_object(data, json_key)
    )