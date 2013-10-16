import os

DEBUG = "DEBUG" in os.environ
SECRET_KEY = os.environ.get("SECRET_KEY", "development")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")
STRIPE_KEY = os.environ.get("STRIPE_KEY")
STRIPE_SECRET = os.environ.get("STRIPE_SECRET")

if ENVIRONMENT == 'test':
    TESTING = True
