
class FiteListModel():
    @classmethod
    def make_list(cls, list_name):

        return cls({
            'name': list_name,
            'is_active': False,
            'fites': ()
        })
        
    def __init__(self, data):
        self.name = data['name']
        self.is_active = data['is_active']
        self.fites = data['fites']

    def is_valid_idx(self, idx, nick):
        if idx < len(self.fites):
            fite = self.fites[idx]
            votes = fite['left_fite']['votes'] + fite['right_fite']['votes']

            return not nick in votes
        else:
            return False


    def dump(self):
        return {
            'name': self.name,
            'is_active': self.is_active,
            'fites': self.fites
        }

class FiteItemModel():
    @classmethod
    def make_item(cls, name):
        return cls({
            'name': name,
            'votes': ()
        })

    def __init__(self, data):
        self.votes = data['votes']
        self.name = data['name']


    def dump(self):
        return {
            'votes': self.votes,
            'name': self.name
        }

class FiteModel():
    @classmethod
    def make_fite(cls, fite):
        return cls({
            'left_fite': fite[0],
            'right_fite': fite[1]
        })


    def __init__(self, data):
        self.left_fite = FiteItemModel.make_item(data['left_fite'])
        self.right_fite = FiteItemModel.make_item(data['right_fite'])

    def dump(self):
        return {
                'left_fite': self.left_fite.dump(),
                'right_fite': self.right_fite.dump(),
        }
