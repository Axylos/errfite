import pytest
from fitedb.fite_client import FiteClient

class TestFiteClient():
    @classmethod
    def setup_class(cls):
        cls.client = FiteClient(is_test=True)

    def test_get_fites(self):
        assert () == self.client.get_all_fites()


    def test_make_fite_list(self):

        self.client.new_fitelist("wat")
        fites = self.client.get_all_fites()
        assert () != fites

        with pytest.raises(Exception):
            self.client.new_fitelist("wat")


        self.client.new_fitelist("foo")


    def test_get_fite_list(self):
        fites = self.client.get_all_fites()
        last_name = fites[1]['name']

        found_fite = self.client.fetch_fitelist(last_name)
        assert last_name == found_fite.name

        assert None == self.client.fetch_fitelist("not valid")

    def test_add_fite_to_list(self):
        fite_list = self.client.fetch_fitelist("foo")
        assert self.client.add_fite("foo", ("broken home", "tea party")) is not None
