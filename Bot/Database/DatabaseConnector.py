import pymongo
from Util.Constants import db_url

database_name = 'morfeo_db'


def connect():
    db_client = pymongo.MongoClient(db_url)
    db = db_client[database_name]
    return db
