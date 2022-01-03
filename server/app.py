import requests
import json
import os
from flask import *
from flask_dance.contrib.google import make_google_blueprint, google
from flask_cors import CORS, cross_origin
from youtube_transcript_api import YouTubeTranscriptApi

GOOGLE_CLIENT_ID = json.loads(open('tokens.json', 'r').read())['web']['client_id']
GOOGLE_CLIENT_SECRET = json.loads(open('tokens.json', 'r').read())['web']['client_secret']
SECRET_KEY = json.loads(open('tokens.json', 'r').read())['nonweb']['secret_key']

class Video:
    def __init__(self, i, a):
        self.id = i
        self.manual = a
        self.captions = []

class Caption:
    def __init__(self, s, e, d, t):
        self.start = s
        self.end = e
        self.duration = d
        self.text = t

def getInfo(videoID):

    try:
        transcriptList = YouTubeTranscriptApi.list_transcripts(videoID)

        foundManual = False
        captionDict = 0
        for transcript in transcriptList:
            if(transcript.is_generated == False and transcript.language == 'English'):
                captionDict = transcript.fetch()
                foundManual = True
                break
            if('English' in transcript.language):
                captionDict = transcript.fetch()

        if(captionDict == 0):
            video = Video(0, False)
            jsonVideo = json.dumps(video, default=lambda o: o.__dict__)
            return jsonVideo

        video = Video(videoID, foundManual)

        for caption in captionDict:
            video.captions.append(Caption(caption['start'], caption['start'] + caption['duration'], caption['duration'], caption['text'].replace(chr(34), '').replace('\n',' ').replace(chr(160), ' ')))

        jsonVideo = json.dumps(video, default=lambda o: o.__dict__)
        return jsonVideo

    except(Exception):
        video = Video(0, False)
        jsonVideo = json.dumps(video, default=lambda o: o.__dict__)
        return jsonVideo

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['TESTING'] = True
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
def api_test(videoID):
    return getInfo(videoID)

@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    # Store in database
    return "You are {email} on Google".format(email=resp.json()["emails"][0]["value"])

if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)
