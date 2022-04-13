import datetime
import logging
import ulid

from settings import InfoMsgs, Config
from pymongo import MongoClient


class MongoDatabase:
    def __init__(self):
        self.app = Config.MONGO_APP
        self.link = Config.MONGO_LINK
        self.db_pass = Config.MONGO_PASS
        self.client = MongoClient(self.app + self.db_pass + self.link)

        # Change these below to the real db and collection names
        self.db = self.client.typerspace
        self.user_collection = self.db.users
        self.stats_collection = self.db.stats

        logging.basicConfig(format="%(asctime)s %(message)s")

    def exception_handler(self, func):
        def inner_function(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(f"Caught error in function: {func.__name__}. Error: {e}")

        return inner_function

    @exception_handler
    def store_user(self, data):
        user_name = data.get("name")
        user_email = data.get("email")
        current_timestamp = datetime.datetime.now()
        user_id = ulid.new().str

        if self.user_collection.find({"name": user_name}).count() == 0:
            self.user_collection.insert_one(
                {
                    "user_id": user_id,
                    "name": user_name,
                    "email": user_email,
                    "created_timestamp": current_timestamp,
                }
            )
            logging.info(
                InfoMsgs.user_added_to_db.format(name=user_name, email=user_email)
            )

        else:
            logging.info(
                InfoMsgs.user_already_in_db.format(name=user_name, email=user_email)
            )

    @exception_handler
    def retrieve_user(self, id):
        return self.user_collection.find_one({"user_id": id})
        return user

    @exception_handler
    def retrieve_stats(self, id):
        return self.stats_collection.find_one({"user_id": id})

    @exception_handler
    def update_stats(self, id, stats):
        return self.stats_collection.update_one({"user_id": id}, {"$set": stats})

    @exception_handler
    def store_stats(self, id, stats):
        return self.stats_collection.insert_one({"user_id": id, **stats})
