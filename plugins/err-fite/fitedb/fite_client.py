from pymongo import MongoClient

from .list_client import FiteListClient
from .fite_model import FiteModel, FiteListModel


TEST_DB_NAME = "err_test_db"
DB_NAME = "fitedb"

class FiteClient(object):
    def __init__(self, is_test=False):
        self.client = MongoClient()
        self.is_test = is_test

        self.setup_db()

    def get_all_fites(self):
        return self.fite_list_client.get_all_fitelists()

    def new_fitelist(self, list_name):
        fite = FiteListModel.make_list(list_name)
        return self.fite_list_client.new_fitelist(fite.dump())

    def fetch_fitelist(self, list_name):
        return self.fite_list_client.get_fitelist(list_name)

    def add_fite(self, list_name, fite):
        fite = FiteModel.make_fite(fite)
        return self.fite_list_client.add_fite(list_name, fite)

    def clean_db(self):
        self.client.drop_database(DB_NAME)

    def setup_db(self):
        if self.is_test is False:
            self.db = self.client[DB_NAME]
        else:
            self.client.drop_database(TEST_DB_NAME)
            self.db = self.client[TEST_DB_NAME]

        self.fite_list_client = FiteListClient(self.db)


    def reset_for_test(self):
        if self.is_test is False:
            self.client.drop_database(TEST_DB_NAME)
            self.is_test = True
            self.setup_db()
