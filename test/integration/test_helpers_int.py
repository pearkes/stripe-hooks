import httpretty
import stripe
from test.base import IntegrationTest
from shared.helpers import format_stripe_object


class TestHelpers(IntegrationTest):

    """Tests for the helpers that require configuration and
    fixtures.
    """

    def test_format_stripe_object(self):
        """Makes sure that it returns something useful for rending in
        an email."""

        httpretty.register_uri(
            httpretty.GET, "https://api.stripe.com/v1/customers/cus_id_fake",
            body=self.fixture('customer.json'))

        customer = stripe.Customer.retrieve("cus_id_fake")
        data = format_stripe_object(customer)

        assert data['description'] == 'test'
