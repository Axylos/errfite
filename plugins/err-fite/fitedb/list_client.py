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


    def get_fitelist(self, list_name):
        fite = self.fitelist.find_one({'name': list_name})

        if fite is None:
            return None

        return FiteListModel(fite)

    def get_current_list(self):
        return self.fitelist.find_one({'is_active': True})

    def deactivate_list(self):
        return self.fitelist.update_many({'is_active': True}, {'$set': {'is_active': False}})

    def vote(self, nick, fite_id, item):
        current_list = self.get_current_list()
        return self.fitelist.find_one_and_update(
            {'name': current_list['name']}, 
            {'$addToSet': {u'fites{}.{}.votes'.format(fite_id, item): nick}},
            return_document=ReturnDocument.AFTER
                )

    def activate_list(self, list_name):
        fite = self.get_fitelist(list_name)

        if fite is not None:
            self.deactivate_list()
            self.fitelist.find_one_and_update({'name': list_name}, {'$set': {'is_active': True}})

            return fite.name


