from test.base import UnitTest
from shared.parser import parse_hook


class TestParser(UnitTest):

    def test_parsing(self):
        assert parse_hook({}) is True
