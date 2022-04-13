import datetime
import logging

from settings import InfoMsgs, Config
from pymongo import MongoClient

class MongoDatabase:
    def __init__(self):
        self.app = Config.MONGO_APP
        self.link = Config.MONGO_LINK
        self.db_pass = Config.MONGO_PASS
        self.client = MongoClient(self.app + self.db_pass + self.link)
        # change these to the real db and collection names
        self.db = self.client.typerspace
        self.collection = self.db.users

        logging.basicConfig(format='%(asctime)s %(message)s')

    def exception_handler(self, func):
        def inner_function(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(f"Caught error in function: {func.__name__}. Error: {e}")
        return inner_function

    @exception_handler
    def store_new_user(self, data):
        user_name = data.get('name')
        user_email = data.get('email')
        if self.collection.find({'name': user_name}).count() == 0:
            current_timestamp = datetime.datetime.now()
            self.collection.insert_one({'name': user_name, 'email': user_email, 'created_timestamp': current_timestamp})
            logging.info(InfoMsgs.user_added_to_db.format(name=user_name, email=user_email))
        else:
            logging.info(InfoMsgs.user_already_in_db.format(name=user_name, email=user_email))
    