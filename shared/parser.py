from helpers import ParseHookFailure


def parse_hook(paylood):
    """Parses a dictionary representation of the stripe webhook
    by requesting a new version of the event by it's ID from the stripe
    API. This is done for security reasons.

    see https://github.com/pearkes/stripe-hooks#security
    """
    raise ParseHookFailure("could not parse webhook")
