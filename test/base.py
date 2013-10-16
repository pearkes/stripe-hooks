from shared.bootstrap import app


class UnitTest(object):

    def setup_method(self, method):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True

    def teardown_method(self, method):
        pass


class IntegrationTest(object):

    def setup_method(self, method):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        # Attach the client
        self.client = app.test_client()

    def teardown_method(self, method):
        pass
