import httpretty
import os
from shared.bootstrap import app


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
