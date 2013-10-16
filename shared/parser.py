import stripe
from helpers import ParseHookFailure


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

    print event.__dict__

    return False
