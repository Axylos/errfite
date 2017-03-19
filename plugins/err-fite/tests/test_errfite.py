import os
from errbot.backends.test import testbot

class TestErrFite(object):
    extra_plugin_dir = '.'

    def test_command(self, testbot):
        testbot.push_message('!fite')
        assert 'fiting' in testbot.pop_message()

    def test_get_fite_list(self, testbot):
        testbot.push_message('!get fites')
        assert "No fites found!" in testbot.pop_message()


