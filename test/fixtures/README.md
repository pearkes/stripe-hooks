## test/fixtures

These are fixtures for supporting mostly the integration tests.

- `events/`: These are JSON responses, mostly taken from Stripe's API
documentation, for each API response from Stripe on the event endpoint.
The files are named according to the event type they are retrieving. This
is used for mocking Stripe in the integration tests. Any event placed
in here will automatically be integration tested, it's dynamic. See
`test_parser.py#test_parser_request_all_events`
- `configuration.json`: This is test configuration, used to bootstrap
the application for a "fully running" environment. All events are active
and configured for both `reciepts` and `notifications`.
- `not_found.json`: A fixture for `404` requests made to the Stripe
API for bad case testing
