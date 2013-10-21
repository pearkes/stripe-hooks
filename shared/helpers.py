import json
import time
from flask import jsonify


def jsonify_with_status(status, *args, **kwargs):
    """Takes a status code and an object to be jsonified and returns a response
    object that can be returned from an API endpoint.
    """
    response = jsonify(*args, **kwargs)
    response.status_code = status
    return response


def datetime_from_epoch(epoch):
    "Converts an epoch timestamp to a human readable time"
    return time.strftime("%a, %d %b %Y %H:%M:%S",
                         time.localtime(epoch))


def format_stripe_object(stripe_object):
    """Returns an array of key-value pairs that can be easily iterated
    in templates.
    """
    ignored_keys = ['livemode', 'object', 'metadata', 'data', 'url']
    date_keys = ['created']

    # Copy the stripe object
    data = stripe_object.to_dict()

    for key in data.keys():
        # If it's a dict we have more to do
        if isinstance(data[key], dict) is True:
            for k in data[key].keys():
                data[key][k] = str(data[key][k])

                # Convert dates for sub-keys
                if k in date_keys:
                    data[key][k] = datetime_from_epoch(data[key])

                # Drop ignored sub-keys
                if k in ignored_keys:
                    del(data[key][k])

            # Join it all to a string
            data[key] = ",".join(data[key].values())

        # Convert dates to human readable
        if key in date_keys:
            data[key] = datetime_from_epoch(data[key])

        # Remove ignored keys
        if key in ignored_keys:
            del(data[key])

    # Make the titles pretty
    for key in data.keys():
        if "_" in key:
            new_key = key.replace("_", " ")
            data[new_key] = data[key]
            del(data[key])

    for key in data.keys():
        print "%s: %s" % (key, data[key])

    return data


def load_configuration(path):
    """Loads the JSON configuration from a path and returns it as a
    dictionary, validating any required attributes.
    """
    data = json.load(open(path))

    if data.get("business") == None:
        raise Exception(
            "Configuration failure: a business attribute is required")
    if data["business"].get("email_address") == None:
        raise Exception(
            "Configuration failure: a business email address is required")
    if data["business"].get("notification_address") == None:
        raise Exception(
            "Configuration failure: a notification address is required")

    return data


class CleanParseException(Exception):

    """An Exception used when a failure parsing the content of a webhook
    is caused, but we should respond to Stripe with a 200
    """
