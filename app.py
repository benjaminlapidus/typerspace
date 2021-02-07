import requests
import json
from flask import *
from youtube_transcript_api import YouTubeTranscriptApi

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

@app.route("/api/<videoID>")
def api_test(videoID):
    return getInfo(videoID)

@app.route("/", methods=['GET'])
def home():
    return "Home"

if __name__ == "__main__":
    app.run(threaded=True, port=5000)