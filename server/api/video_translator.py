import json

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

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        found_manual = False
        caption_dict = 0
        for transcript in transcript_list:
            if(transcript.is_generated == False and transcript.language == 'English'):
                caption_dict = transcript.fetch()
                found_manual = True
                break
            if('English' in transcript.language):
                caption_dict = transcript.fetch()

        if(caption_dict == 0):
            video = Video(0, False)
            json_video = json.dumps(video, default=lambda o: o.__dict__)
            return json_video

        video = Video(video_id, found_manual)

        for caption in caption_dict:
            video.captions.append(Caption(caption['start'], caption['start'] + caption['duration'], caption['duration'], caption['text'].replace(chr(34), '').replace('\n',' ').replace(chr(160), ' ')))

        json_video = json.dumps(video, default=lambda o: o.__dict__)
        return json_video

    except Exception:
        video = Video(0, False)
        json_video = json.dumps(video, default=lambda o: o.__dict__)
        return json_video