import httpretty
import os
from shared.bootstrap import app
from shared.helpers import load_configuration


class UnitTest(object):

    def setup_method(self, method):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        httpretty.enable()

    def teardown_method(self, method):
        httpretty.disable()

    def fixture(self, path):
        path = os.path.join("test/fixtures/", path)
        return open(path).read()


class IntegrationTest(object):

    def setup_method(self, method):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        app.config['email'] = load_configuration(os.path.join("test/fixtures/", "configuration.json"))
        # Attach the client
        self.client = app.test_client()
        # Turn on HTTP mocking
        httpretty.enable()

    def teardown_method(self, method):
        # Turn off HTTP Mocking
        httpretty.disable()

    def fixture(self, path):
        path = os.path.join("test/fixtures/", path)
        return open(path).read()
