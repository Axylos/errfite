from pymongo import MongoClient

class FiteClient(object):
    def __init__(self):
        print("ran")
        self.client = MongoClient()
        pass

    def foo(self):
        return "bar"
