import json
from flask import jsonify


def jsonify_with_status(status, *args, **kwargs):
    """Takes a status code and an object to be jsonified and returns a response
    object that can be returned from an API endpoint.
    """
    response = jsonify(*args, **kwargs)
    response.status_code = status
    return response


def load_configuration(path):
    """Loads the JSON configuration from a path and returns it as a
    dictionary, validating any required attributes.
    """
    data = json.load(open(path))

    if not data.get("business"):
        Exception("Configuration failure: a business attribute is required")
    if not data.get("business").get("email_address"):
        Exception("Configuration failure: a business email is required")
    if not data.get("business").get("notification_address"):
        Exception("Configuration failure: a notification address is required")

    return data


class ParseHookFailure(Exception):

    """An Exception used when a failure parsing the content of a webhook
    is caused.
    """
    pass
