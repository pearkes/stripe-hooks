## stripe-hooks

This is a Python web application to recieve [Webhooks](https://stripe.com/docs/webhooks)
from Stripe and send emails accordingly.

There are two types of emails:

- Notifcations, sent to administrators
- Receipts, sent to customers

It's easy to deploy and you shouldn't need to touch Python to configure it.

### Configuration

All of the configuration is done in JSON in the [`configuration.json`](configuration.json)
file.

All receipts and notifications are **off by default**. To activate
a notification or receipt, simply create a new key, named by the
event type (the list can be found [here](https://stripe.com/docs/api#event_types))
and formatted like this:

```json
    "charge.failed": {
      "active": true,
      "subject": "Oh nos! A Charge Has Failed!"
    }
```

`subject` is optional. By default, the email subject will be the type,
periods replacing spaces and titlecased, prefixed with your
business name (if it exists) like so: `charge.failed -> [Acme Inc.] Charge Failed`.

Everything falls back to safe, generic defaults, like not showing a business name
if it doesn't exist.

Full configuration could look something like this:

```json
{
  "business": {
    "name": "Acme, Inc.",
    "signoff": "The Acme Team",
    "email": "Acme Support Team <support@example.com>"
  },
  "notifications": {
    "balance.available": {
      "active": true
      "subject": "Dat chedda is available..."
    },
    "charge.succeeded": {
      "active": true
    },
    "charge.failed": {
      "active": true
    },
    "charge.refunded": {
      "active": true
    }
  },
  "receipts": {
    "invoice.created": {
      "active": true,
      "subject": "New Invoice"
    }
  }
}
```

### Security

In order to avoid fraudulent requests made to the `/webhook/recieve` endpoint,
the only attribute trusted in the payload is the event ID. This ID is then
used to request the event directly from Stripe with proper authentication.

### Contributing

See the [Contributing Guide](CONTRIBUTING.md).
