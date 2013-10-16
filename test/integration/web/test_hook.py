import json
import httpretty
from test.base import IntegrationTest


class TestWebhook(IntegrationTest):

    def test_recieve(self):
        "Posts a fake stripe webhook payload to the API"

        httpretty.register_uri(httpretty.GET,
                               "https://api.stripe.com/v1/events/evt_2lQ5CTBYawXWVi",
                               body=self.fixture('events/customer_created.json'))

        data = json.dumps({'id': "evt_2lQ5CTBYawXWVi"})

        rv = self.client.post(
            "/webhook/recieve", data=data, content_type='application/json')

        assert rv.status_code == 200
        assert b'success' in rv.data
