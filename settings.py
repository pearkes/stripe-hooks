import os

DEBUG = "DEBUG" in os.environ
SECRET_KEY = os.environ.get("SECRET_KEY", "development")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")
STRIPE_KEY = os.environ.get("STRIPE_KEY", "test")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY", "test")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY", "test")

if ENVIRONMENT == 'test':
    TESTING = True
