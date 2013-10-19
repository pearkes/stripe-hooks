import stripe
from .app import app
from helpers import ParseHookFailure
from shared.mail import send_notification, send_receipt


def parse_hook(payload):
    """Parses a dictionary representation of the stripe webhook
    by requesting a new version of the event by it's ID from the stripe
    API. This is done for security reasons.

    See https://github.com/pearkes/stripe-hooks#security
    """
    # Request the event from Stripe, raises stripe.InvalidRequestError if
    # not found.
    event = stripe.Event.retrieve(payload.get("id"))

    # Determine what type of event it is and send any nots/receipts
    determine_event_type(event)


def determine_event_type(event):
    "Determines what type of hook an event is"

    config = app.config['email']

    if config['notifications'].get(event.type):
        parse_notification(event)

    if config['receipts'].get(event.type):
        parse_receipt(event)


def parse_notification(event):
    "Parse the details of an event for a notification"
    send_notification(event.type, event.data.object)


def parse_receipt(event):
    "Parse the details of an event for a receipt"
    send_receipt(event.type, event.data.object)
