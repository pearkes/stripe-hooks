import json
import tempfile
from test.base import UnitTest
from shared.helpers import load_configuration


class TestHelpers(UnitTest):

    def test_load_configuration(self):
        "Tests that the load_coniguration method loads the config correctly"

        temp_file = tempfile.NamedTemporaryFile()
        test_conf = {
            "business": {
                "email_address": "foobar@gmail.com",
                "name": "Foo Bar",
                "notification_address": "foobar@gmail.com"
            }
        }
        temp_file.write(json.dumps(test_conf))
        temp_file.seek(0)

        conf = load_configuration(temp_file.name)
        assert conf == test_conf
