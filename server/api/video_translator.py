import json
import logging

from settings import InfoMsgs
from youtube_transcript_api import YouTubeTranscriptApi


class Transcriber:
    def __init__(self):
        logging.basicConfig(format="%(asctime)s %(message)s")

    class Video:
        def __init__(self, id, manual):
            self.id = id
            self.manual = manual
            self.captions = []

    class Caption:
        def __init__(self, start, end, duration, text):
            self.start = start
            self.end = end
            self.duration = duration
            self.text = text

    def get_transcript(self, video_id):
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            found_manual = False
            caption_dict = 0
            for transcript in transcript_list:
                if (
                    transcript.is_generated == False
                    and transcript.language == "English"
                ):
                    caption_dict = transcript.fetch()
                    found_manual = True
                    break
                if "English" in transcript.language:
                    caption_dict = transcript.fetch()

            if caption_dict == 0:
                video = self.Video(0, False)
                json_video = json.dumps(video, default=lambda o: o.__dict__)
                return json_video

            video = self.Video(video_id, found_manual)

            for caption in caption_dict:
                video.captions.append(
                    self.Caption(
                        caption["start"],
                        caption["start"] + caption["duration"],
                        caption["duration"],
                        caption["text"]
                        .replace(chr(34), "")
                        .replace("\n", " ")
                        .replace(chr(160), " "),
                    )
                )

            json_video = json.dumps(video, default=lambda o: o.__dict__)
            logging.info(InfoMsgs.transcribed_video.format(video_id=video_id))

            return json_video

        except Exception as e:
            video = self.Video(0, False)

            json_video = json.dumps(video, default=lambda o: o.__dict__)
            logging.info(
                InfoMsgs.transcribed_video_error.format(video_id=video_id, error=e)
            )

            return json_video
