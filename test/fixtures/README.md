## test/fixtures

These are fixtures for supporting mostly the integration tests.

- `event_types.json`: A list of event types taken from Stripe's
[documentation](https://stripe.com/docs/api#event_types). This fixture
is used to direct integration tests for the various tests. Adding a
event requires you to create a new fixture for that events request, as
well.
- `events/`: These are JSON responses, mostly taken from Stripe's API
documentation, for each API response from Stripe on the event endpoint.
The files are named according to the event type they are retrieving. This
is used for mocking Stripe in the integration tests.
- `configuration.json`: This is test configuration, used to bootstrap
the application for a "fully running" environment. All events are active
and configured for both `reciepts` and `notifications`.
