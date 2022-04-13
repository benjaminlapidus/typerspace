import secrets
import os

from flask import Flask
from flask_dance.contrib.google import make_google_blueprint, google
from flask_cors import CORS, cross_origin
from api.video_translator import get_transcript
from oauth.authorization import check_if_auth
from settings import Config

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

blueprint = make_google_blueprint(
    client_id=Config.GOOGLE_CLIENT_ID,
    client_secret=Config.GOOGLE_CLIENT_SECRET,
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
