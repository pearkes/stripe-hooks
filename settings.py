import os

DEBUG = "DEBUG" in os.environ
SECRET_KEY = os.environ.get("SECRET_KEY", "development")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")
STRIPE_KEY = os.environ.get("STRIPE_KEY")
STRIPE_SECRET = os.environ.get("STRIPE_SECRET")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")

if ENVIRONMENT == 'test':
    TESTING = True
