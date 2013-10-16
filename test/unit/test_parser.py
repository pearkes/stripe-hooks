import httpretty
from test.base import UnitTest
from shared.parser import parse_hook


class TestParser(UnitTest):

    def test_parsing(self):
        httpretty.register_uri(
            httpretty.GET, "https://api.stripe.com/v1/events/evt_2lQ5CTBYawXWVi",
            body=self.fixture('events/customer_created.json'))

        assert parse_hook({"id": "evt_2lQ5CTBYawXWVi"}) is True
