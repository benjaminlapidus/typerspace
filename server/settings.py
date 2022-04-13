import os
import secrets

class Config:
    GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']
    GOOGLE_CLIENT_SECRET = os.environ['GOOGLE_CLIENT_SECRET']
    SECRET_KEY = secrets.token_urlsafe(16)

    MONGO_APP = os.environ['MONGO_APP']
    MONGO_LINK = os.environ['MONGO_LINK']
    MONGO_PASS = os.environ['MONGO_PASS']

class InfoMsgs:
    authorized_user = 'User logged in with name: {name} and email: {email}.'
    unsuccessful_login = "User attempted login but failed."
    user_already_in_db = "User [{name}, {email}] already exists in DB."
    user_added_to_db = "User [{name}, {email}] added to DB."