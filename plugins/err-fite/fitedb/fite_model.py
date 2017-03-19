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

    def dump(self):
        return {
            'name': self.name,
            'is_active': self.is_active,
            'fites': self.fites
        }

class FiteModel():
    @classmethod
    def make_fite(cls, fite):
        return cls({
            'left_fite': fite[0],
            'right_fite': fite[1],
            'votes': ()
        })


    def __init__(self, data):
        self.left_fite = data['left_fite']
        self.right_fite = data['right_fite']
        self.votes = data['votes']

    def dump(self):
        return {
                'left_fite': self.left_fite,
                'right_fite': self.right_fite,
                'votes': self.votes
        }
