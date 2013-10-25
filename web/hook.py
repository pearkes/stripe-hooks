from flask import Blueprint, request
from stripe import InvalidRequestError
from shared.helpers import jsonify_with_status, CleanParseException
from shared.parser import parse_hook

hook = Blueprint("hook", __name__)


@hook.route("/receive", methods=["POST"])
def receieve_hook():
    """
    Path:       /webhook/receive
    Method:     POST
    """
    # Abort if we're not sent JSON
    if not request.json:
        return jsonify_with_status(406, {'error': 'Requires application/json'})

    # If the event doesn't have a id, it's not an event
    # https://stripe.com/docs/api#events
    if not request.json.get("id"):
        return jsonify_with_status(406, {'error': 'Does not have an id'})

    try:
        parse_hook(request.json)
    except InvalidRequestError as e:
        # If the hook failed to parse, send back why to stripe
        # This will be visible in your dashboard
        return jsonify_with_status(406, {'error': str(e)})
    except CleanParseException as e:
        # If the hook failed to parse, but we don't want it
        # to try again, send back why and a 200 so Stripe stops trying.
        return jsonify_with_status(200, {'error': str(e)})

    return jsonify_with_status(200, {'success': True})
