import pymongo
from setup.config import config

class Database(object):
    DATABASE= None

    @staticmethod
    def initialize(db):
        client=pymongo.MongoClient(config["dbURL"])
        Database.DATABASE=client[db]

    @staticmethod
    def insert(collection, doc):
        return Database.DATABASE[collection].insert(doc)

    @staticmethod
    def updateOne(collection, **kwargs):
        return Database.DATABASE[collection].update_one(filter=kwargs["filter"],
                                                        update=kwargs["update"],
                                                        upsert=kwargs["upsert"])

    @staticmethod
    def find(collection, **kwargs):
        return Database.DATABASE[collection].find(filter=kwargs["filter"],
                                                  projection=kwargs["projection"],
                                                  limit=kwargs["limit"],
                                                  sort=kwargs["sort"])
