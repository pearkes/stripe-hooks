import httpretty
import glob
import json
import pytest
from stripe import InvalidRequestError
from test.base import UnitTest
from shared.parser import parse_hook


class TestParser(UnitTest):

    """Parser tests simply mock the Stripe API, pass in a fake event and
    expects that the parser properly renders text and HTML templates. Exceptions
    will be raised if things aren't going well all the way down to the template
    rendering, hence a lack of assertions. No exception means things went well"""

    def test_parser_request_all_events(self):
        """This test lists all of the mocked events in the test/fixtures/events
        directory, and correspondingly kicks off a parse, retrieve and render
        integration test. This means, to add a new event, all you need to do
        is drop in the JSON representation and this test will pick it up."""

        event_types = glob.glob("test/fixtures/events/*.json")

        for event_path in event_types:
            event = json.load(open(event_path))

            try:
                event_type = event["type"].replace(".", "_")
            except KeyError:
                raise Exception(
                    "Your fixture is badly formatted and does not contain a type: %s" % (event_path))

            httpretty.register_uri(
                httpretty.GET, "https://api.stripe.com/v1/events/evt_id_fake",
                body=self.fixture('events/%s.json' % event_type))

            parse_hook({"id": "evt_id_fake"})

    def test_parser_bad_id(self):
        "Tests parsing a bad id"

        httpretty.register_uri(
            httpretty.GET, "https://api.stripe.com/v1/events/evt_id_fake",
            body=self.fixture('not_found.json'), status=404)

        with pytest.raises(InvalidRequestError):
            parse_hook({"id": "evt_id_fake"})

    def test_parser_no_id(self):
        "Tests parsing no id"

        with pytest.raises(InvalidRequestError):
            parse_hook({})
