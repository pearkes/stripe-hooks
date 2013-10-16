import stripe
from .app import app
from helpers import ParseHookFailure
from shared.mail import send_notification


def parse_hook(payload):
    """Parses a dictionary representation of the stripe webhook
    by requesting a new version of the event by it's ID from the stripe
    API. This is done for security reasons.

    See https://github.com/pearkes/stripe-hooks#security
    """
    # Request the event from Stripe
    event = stripe.Event.retrieve(payload["id"])

    if not event:
        raise ParseHookFailure("event does not exist")

    config = app.config['email']

    if config['notifications'].get(event.type):
        parse_notification(event)

    if config['receipts'].get(event.type):
        parse_receipt(event)

    return False


def parse_notification(event):
    """Parses a notification as it was enabled and ready to be sent.
    """
    send_notification(event.type, event.data.object)
    pass


def parse_receipt(event):
    """Parses a notification as it was enabled and ready to be sent.
    """
    raise ParseHookFailure("failed!")
    pass
