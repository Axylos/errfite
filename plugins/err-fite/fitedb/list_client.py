from .fite_model import FiteModel, FiteListModel
from pymongo import ReturnDocument

class FiteListClient(object):
    def __init__(self, db):
        self.fitelist = db.fitelist
        self.fitelist.create_index('name', unique=True)

    def get_all_fitelists(self):
        return tuple(self.fitelist.find())


    def new_fitelist(self, fite):
        return self.fitelist.insert_one(fite)

    def add_fite(self, list_name, fite):
        new_fite = self.fitelist.find_one_and_update(
                {'name': list_name},
                {'$addToSet': {'fites': fite.dump()}},
                return_document=ReturnDocument.AFTER
        )

        return new_fite
        return new_fite is not None


    def get_fitelist(self, list_name):
        fite = self.fitelist.find_one({'name': list_name})

        if fite is None:
            return None

        return FiteListModel(fite)
