import json
from test.base import IntegrationTest


class TestWebhook(IntegrationTest):

    def test_recieve(self):
        "Posts a fake stripe webhook payload to the API"
        data = json.dumps({'id': "foobar_stripe_id"})

        rv = self.client.post("/webhook/recieve", data=data, content_type='application/json')

        assert rv.status_code == 200
        assert b'success' in rv.data
