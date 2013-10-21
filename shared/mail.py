import boto
import time
import datetime
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from shared.helpers import humanize_date, humanize_money

from .app import app

# Global variables in the Jinga templates.
globals = {'business': app.config['email'][
    'business'], 'humanize_date': humanize_date, 'humanize_money': humanize_money}

notify_templates = Environment(
    loader=FileSystemLoader('stripe-hooks-emails/notifications'), undefined=StrictUndefined)
notify_templates.globals = globals

receipt_templates = Environment(
    loader=FileSystemLoader('stripe-hooks-emails/receipts'), undefined=StrictUndefined)
receipt_templates.globals = globals


def ses_connection():
    return boto.connect_ses(
        aws_access_key_id=app.config['AWS_ACCESS_KEY'],
        aws_secret_access_key=app.config['AWS_SECRET_KEY'])


def send_receipt(key, recipient, data=None):
    "Sends a receipt type of notification to a user"
    # If we don't have an ID, which we shouldn't, default it.
    if data is None:
        data = {"id": "no_event"}

    txt_template = receipt_templates.get_template(
        '%s.%s' % (key.replace(".", "/"), 'txt'))
    html_template = receipt_templates.get_template(
        '%s.%s' % (key.replace(".", "/"), 'html'))

    # Configuration for the business
    business = app.config['email']['business']

    # Get the configuration for the type of event
    event_conf = app.config['email']['receipts'].get(key)

    if event_conf.get("subject") is None:
        subject_title = "%s (%s)" % (key.replace(".", " ").title(), data["id"])
    else:
        subject_title = event_conf["subject"]

    from_address = business['email_address']
    subject = "[%s] %s" % (business['name'], subject_title)

    # Add some namespaced helpers to the data
    meta = {}
    meta['subject'] = subject
    meta['current_timestamp'] = datetime.datetime.now()

    txt_rendered = txt_template.render(data=data, meta=meta)
    html_rendered = html_template.render(data=data, meta=meta)

    if app.config.get("TESTING") is True:
        # Don't send while unit/integration testing
        return

    conn = ses_connection()
    # Send the actual email
    conn.send_email(
        from_address,
        subject,
        txt_rendered,
        [recipient],
        html_body=html_rendered)


def send_notification(key, data=None):
    "Sends a notification to an administrator"

    txt_template = notify_templates.get_template(
        '%s.%s' % (key.replace(".", "/"), 'txt'))
    html_template = notify_templates.get_template(
        '%s.%s' % (key.replace(".", "/"), 'html'))

    # Configuration for the business
    business = app.config['email']['business']

    # Get the configuration for the type of event
    event_conf = app.config['email']['notifications'].get(key)

    # Default the subject if there isn't one specified
    if event_conf.get("subject") is None:
        subject_title = "%s (%s)" % (
            key.replace(".", " ").title(), data.get("id", int(time.time())))
    else:
        subject_title = event_conf["subject"]

    from_address = business['email_address']
    subject = "[Stripe Notification] %s" % (subject_title)

    # Add some namespaced helpers to the data
    meta = {}
    meta['subject'] = subject
    meta['current_timestamp'] = datetime.datetime.now()

    txt_rendered = txt_template.render(data=data, meta=meta)
    html_rendered = html_template.render(data=data, meta=meta)

    if app.config.get("TESTING") is True:
        # Don't send while unit/integration testing
        return

    conn = ses_connection()
    # Send the actual email
    conn.send_email(
        from_address,
        subject,
        txt_rendered,
        [business['notification_address']],
        html_body=html_rendered)
