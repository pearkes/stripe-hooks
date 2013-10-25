import json
import httpretty
from test.base import IntegrationTest


class TestWebhook(IntegrationTest):

    def test_receive(self):
        "Posts a fake stripe webhook payload to the API"

        httpretty.register_uri(httpretty.GET,
                               "https://api.stripe.com/v1/events/evt_2lQbUzojdEOlna",
                               body=self.fixture('events/customer_created.json'))

        data = json.dumps({'id': "evt_2lQbUzojdEOlna"})

        rv = self.client.post(
            "/webhook/receive", data=data, content_type='application/json')

        assert rv.status_code == 200
        assert b'success' in rv.data

    def test_receive_bad(self):
        "Posts a fake stripe webhook payload to the API with a bad id"

        httpretty.register_uri(
            httpretty.GET, "https://api.stripe.com/v1/events/evt_id_fake",
            body=self.fixture('not_found.json'), status=404)

        data = json.dumps({'id': "evt_id_fake"})

        rv = self.client.post(
            "/webhook/receive", data=data, content_type='application/json')

        assert rv.status_code == 406
        assert b'No such event' in rv.data
