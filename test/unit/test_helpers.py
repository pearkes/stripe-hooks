import json
import tempfile
import pytest
from test.base import UnitTest
from shared.helpers import load_configuration, datetime_from_epoch


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

    def test_load_configuration_incomplete(self):
        "Raises proper errors for an incomplete configuration"

        temp_file = tempfile.NamedTemporaryFile()
        test_conf = {
            "business": {
                "name": "Foo Bar",
                "notification_address": "foobar@gmail.com"
            }
        }
        temp_file.write(json.dumps(test_conf))
        temp_file.seek(0)

        with pytest.raises(Exception):
            load_configuration(temp_file.name)

    def test_datetime_from_epoch(self):
        formatted = datetime_from_epoch(1382194639)
        assert formatted == "Sat, 19 Oct 2013 07:57:19"
