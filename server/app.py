import secrets
import json
import os

from flask import Flask
from flask_dance.contrib.google import make_google_blueprint, google
from flask_cors import CORS, cross_origin
from api.video_translator import get_transcript
from oauth.authorization import check_if_auth


GOOGLE_CLIENT_ID = json.loads(open('tokens.json', 'r').read())['web']['client_id']
GOOGLE_CLIENT_SECRET = json.loads(open('tokens.json', 'r').read())['web']['client_secret']
SECRET_KEY = secrets.token_urlsafe(16)

app = Flask(__name__)
app.secret_key = SECRET_KEY
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

blueprint = make_google_blueprint(
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    scope=["profile", "email"]
)

app.register_blueprint(blueprint, url_prefix='/login')

@cross_origin()
@app.route("/api/<videoID>")
def get_video_transcript(video_id):
    return get_transcript(video_id)

@app.route("/")
def index():
    return check_if_auth()

if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)
