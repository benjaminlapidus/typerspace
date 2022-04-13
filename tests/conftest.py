import pytest
import json

from youtube_transcript_api import YouTubeTranscriptApi


@pytest.fixture
def request_youtube_api():
    def wrapper(videoID):
        return YouTubeTranscriptApi.list_transcripts(videoID)

    return wrapper


@pytest.fixture
def mock_api_get_video_transcript(request_youtube_api):
    def wrapper(video_id):
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

        transcript_list = request_youtube_api(video_id)

        found_manual = False
        caption_dict = 0
        for transcript in transcript_list:
            if transcript.is_generated == False and transcript.language == "English":
                caption_dict = transcript.fetch()
                found_manual = True
                break
            if "English" in transcript.language:
                caption_dict = transcript.fetch()

        if caption_dict == 0:
            video = Video(0, False)
            json_video = json.dumps(video, default=lambda o: o.__dict__)
            return json_video

        video = Video(video_id, found_manual)

        for caption in caption_dict:
            video.captions.append(
                Caption(
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
        return json_video

    return wrapper


# https://www.youtube.com/watch?v=h6fcK_fRYaI
@pytest.fixture
def mock_api_response():
    return [
        {
            "start": 3.0,
            "end": 5.4,
            "duration": 2.4,
            "text": "You were on your way home, when you died.",
        },
        {
            "start": 6.36,
            "end": 7.74,
            "duration": 1.38,
            "text": "It was a car accident.",
        },
        {
            "start": 9.2,
            "end": 11.2,
            "duration": 2.0,
            "text": "Nothing particularly remarkable.",
        },
        {
            "start": 11.64,
            "end": 12.96,
            "duration": 1.32,
            "text": "But fatal, none the less.",
        },
        {
            "start": 13.88,
            "end": 15.260000000000002,
            "duration": 1.38,
            "text": "It was a painless death.",
        },
        {
            "start": 15.74,
            "end": 19.28,
            "duration": 3.54,
            "text": "The medics tried their best to save you... but to no avail.",
        },
        {
            "start": 20.18,
            "end": 24.42,
            "duration": 4.24,
            "text": "Your body was so utterly shattered, you were better off. Trust me.",
        },
        {
            "start": 25.46,
            "end": 27.46,
            "duration": 2.0,
            "text": "And that's when you met me.",
        },
        {"start": 28.56, "end": 29.2, "duration": 0.64, "text": "What happened?"},
        {"start": 30.58, "end": 31.08, "duration": 0.5, "text": "Where am I?"},
        {"start": 32.12, "end": 32.62, "duration": 0.5, "text": "You died."},
        {
            "start": 33.1,
            "end": 34.7,
            "duration": 1.6,
            "text": "I said, matter of factly.",
        },
        {
            "start": 35.5,
            "end": 36.96,
            "duration": 1.46,
            "text": "No point in mincing words.",
        },
        {
            "start": 37.6,
            "end": 40.120000000000005,
            "duration": 2.52,
            "text": "There was... there was a truck.",
        },
        {"start": 40.64, "end": 41.74, "duration": 1.1, "text": "And it was skidding."},
        {"start": 43.2, "end": 43.7, "duration": 0.5, "text": "Yes."},
        {"start": 44.72, "end": 46.54, "duration": 1.82, "text": "I... I died?"},
        {"start": 47.72, "end": 48.22, "duration": 0.5, "text": "Yes."},
        {
            "start": 49.0,
            "end": 50.74,
            "duration": 1.74,
            "text": "But don't feel bad about it.",
        },
        {"start": 51.4, "end": 52.36, "duration": 0.96, "text": "Everyone dies."},
        {"start": 53.4, "end": 54.3, "duration": 0.9, "text": "You looked around."},
        {
            "start": 55.08,
            "end": 56.86,
            "duration": 1.78,
            "text": "There was.. nothingness.",
        },
        {
            "start": 57.24,
            "end": 58.440000000000005,
            "duration": 1.2,
            "text": "Just you, and me.",
        },
        {"start": 59.94, "end": 61.08, "duration": 1.14, "text": "What is this place?"},
        {
            "start": 62.56,
            "end": 64.0,
            "duration": 1.44,
            "text": "Is this, the afterlife?",
        },
        {"start": 64.92, "end": 65.98, "duration": 1.06, "text": "More or less."},
        {
            "start": 67.08,
            "end": 68.39999999999999,
            "duration": 1.32,
            "text": "Are you.. God?",
        },
        {"start": 69.42, "end": 69.92, "duration": 0.5, "text": "Yes."},
        {"start": 70.42, "end": 70.98, "duration": 0.56, "text": "I'm God."},
        {"start": 72.7, "end": 73.2, "duration": 0.5, "text": "My kids.."},
        {"start": 73.94, "end": 74.48, "duration": 0.54, "text": "My wife..."},
        {
            "start": 76.2,
            "end": 76.88000000000001,
            "duration": 0.68,
            "text": "What about them?",
        },
        {
            "start": 78.56,
            "end": 79.76,
            "duration": 1.2,
            "text": "Will they be alright?",
        },
        {
            "start": 81.2,
            "end": 83.02,
            "duration": 1.82,
            "text": "That's what I like to see, I said.",
        },
        {
            "start": 83.68,
            "end": 86.88000000000001,
            "duration": 3.2,
            "text": "You just died, and your main concern is for your family.",
        },
        {
            "start": 87.42,
            "end": 89.34,
            "duration": 1.92,
            "text": "That's good stuff right there.",
        },
        {
            "start": 90.5,
            "end": 92.2,
            "duration": 1.7,
            "text": "You looked at me with fascination.",
        },
        {
            "start": 92.82,
            "end": 95.38,
            "duration": 2.56,
            "text": "To you, I didn't look like God.",
        },
        {
            "start": 95.84,
            "end": 98.76,
            "duration": 2.92,
            "text": "I just looked like some man, or possibly a woman.",
        },
        {
            "start": 99.46,
            "end": 101.41999999999999,
            "duration": 1.96,
            "text": "Some vague authority figure maybe.",
        },
        {
            "start": 103.78,
            "end": 104.76,
            "duration": 0.98,
            "text": "Don't worry, I said.",
        },
        {"start": 105.22, "end": 106.1, "duration": 0.88, "text": "They'll be fine."},
        {
            "start": 106.46,
            "end": 109.61999999999999,
            "duration": 3.16,
            "text": "Your kids will remember you as perfect in every way.",
        },
        {
            "start": 110.48,
            "end": 113.36,
            "duration": 2.88,
            "text": "They didn't have time to grow contemptuous of you.",
        },
        {
            "start": 114.1,
            "end": 116.33999999999999,
            "duration": 2.24,
            "text": "Your wife will cry on the outside.",
        },
        {
            "start": 116.8,
            "end": 118.5,
            "duration": 1.7,
            "text": "But will be secretly relieved.",
        },
        {
            "start": 120.02,
            "end": 122.83999999999999,
            "duration": 2.82,
            "text": "To be fair, your marriage was falling apart.",
        },
        {
            "start": 123.6,
            "end": 128.57999999999998,
            "duration": 4.98,
            "text": "If it's any consolation, she'll feel very guilty for feeling relieved.",
        },
        {"start": 129.56, "end": 130.06, "duration": 0.5, "text": "Oh.."},
        {
            "start": 130.88,
            "end": 132.16,
            "duration": 1.28,
            "text": "So what happens now?",
        },
        {
            "start": 133.02,
            "end": 135.70000000000002,
            "duration": 2.68,
            "text": "Do I go to Heaven? Or Hell or something?",
        },
        {"start": 136.96, "end": 137.46, "duration": 0.5, "text": "Neither."},
        {
            "start": 138.06,
            "end": 139.6,
            "duration": 1.54,
            "text": "You'll be reincarnated.",
        },
        {"start": 140.96, "end": 141.46, "duration": 0.5, "text": "Ah.."},
        {
            "start": 142.92,
            "end": 144.55999999999997,
            "duration": 1.64,
            "text": "So the Hindus were right!",
        },
        {
            "start": 145.28,
            "end": 147.34,
            "duration": 2.06,
            "text": "All religions are right in their own way.",
        },
        {"start": 148.66, "end": 149.32, "duration": 0.66, "text": "Walk with me."},
        {
            "start": 151.1,
            "end": 153.92,
            "duration": 2.82,
            "text": "You followed along as we strolled through the void.",
        },
        {
            "start": 155.68,
            "end": 156.44,
            "duration": 0.76,
            "text": "Where are we going?",
        },
        {
            "start": 157.38,
            "end": 158.38,
            "duration": 1.0,
            "text": "No where in particular.",
        },
        {
            "start": 158.78,
            "end": 160.72,
            "duration": 1.94,
            "text": "It's just nice to talk while we walk.",
        },
        {
            "start": 162.24,
            "end": 164.16,
            "duration": 1.92,
            "text": "So, what's the point then?",
        },
        {
            "start": 165.22,
            "end": 168.58,
            "duration": 3.36,
            "text": "When I get reborn, I'll just be a blank slate right?",
        },
        {"start": 169.76, "end": 170.26, "duration": 0.5, "text": "A baby?"},
        {
            "start": 171.14,
            "end": 175.7,
            "duration": 4.56,
            "text": "So, all my experiences and everything... everything I did in this life...",
        },
        {"start": 176.04, "end": 176.54, "duration": 0.5, "text": "Won't matter..."},
        {"start": 177.6, "end": 178.42, "duration": 0.82, "text": "Not so."},
        {
            "start": 179.14,
            "end": 184.5,
            "duration": 5.36,
            "text": "You have within you, all the knowledge and experiences of all your past lives.",
        },
        {
            "start": 185.0,
            "end": 186.78,
            "duration": 1.78,
            "text": "You just don't remember them right now.",
        },
        {
            "start": 188.22,
            "end": 191.0,
            "duration": 2.78,
            "text": "I stopped walking, and took you by the shoulders.",
        },
        {
            "start": 191.64,
            "end": 197.29999999999998,
            "duration": 5.66,
            "text": "Your soul is more magnificent, beautiful, and gigantic than you can possibly imagine.",
        },
        {
            "start": 198.52,
            "end": 202.38000000000002,
            "duration": 3.86,
            "text": "A human mind can only contain a tiny fraction of what you are.",
        },
        {
            "start": 203.22,
            "end": 205.92,
            "duration": 2.7,
            "text": "It's like sticking your finger in a glass of water.",
        },
        {
            "start": 206.24,
            "end": 207.52,
            "duration": 1.28,
            "text": "To see if it's hot or cold.",
        },
        {
            "start": 208.34,
            "end": 215.88,
            "duration": 7.54,
            "text": "You put a tiny part of yourself into the vessel, and when you bring it back out, you've gained all the experiences it had.",
        },
        {
            "start": 216.86,
            "end": 219.5,
            "duration": 2.64,
            "text": "You've been in a human for the last 48 years.",
        },
        {
            "start": 219.94,
            "end": 224.35999999999999,
            "duration": 4.42,
            "text": "So you haven't stretched out yet and felt the rest of your immense consciousness.",
        },
        {
            "start": 225.46,
            "end": 229.36,
            "duration": 3.9,
            "text": "If we hung out here for long enough, you'd start remembering everything.",
        },
        {
            "start": 229.96,
            "end": 232.28,
            "duration": 2.32,
            "text": "But there's not point to doing that between each life.",
        },
        {
            "start": 234.06,
            "end": 236.46,
            "duration": 2.4,
            "text": "How many times have I been reincarnated then?",
        },
        {
            "start": 237.8,
            "end": 239.8,
            "duration": 2.0,
            "text": "Oh, lots! Lots and lots!",
        },
        {
            "start": 240.22,
            "end": 242.3,
            "duration": 2.08,
            "text": "And into lots of different lives.",
        },
        {
            "start": 242.76,
            "end": 247.54,
            "duration": 4.78,
            "text": "This time around, you'll be a Chinese peasant girl in 540 A.D",
        },
        {"start": 249.16, "end": 250.62, "duration": 1.46, "text": "Wait... What?!"},
        {
            "start": 251.2,
            "end": 252.98,
            "duration": 1.78,
            "text": "You're sending me back in time?",
        },
        {
            "start": 254.34,
            "end": 255.88,
            "duration": 1.54,
            "text": "Well I guess technically.",
        },
        {
            "start": 256.56,
            "end": 259.9,
            "duration": 3.34,
            "text": "Time as you know it, only exists in your universe.",
        },
        {
            "start": 260.5,
            "end": 262.06,
            "duration": 1.56,
            "text": "Things are different where I come from.",
        },
        {
            "start": 263.56,
            "end": 265.3,
            "duration": 1.74,
            "text": "Where... where you come from?",
        },
        {
            "start": 266.52,
            "end": 269.62,
            "duration": 3.1,
            "text": "Oh sure, I come from somewhere. Somewhere else.",
        },
        {
            "start": 270.04,
            "end": 271.8,
            "duration": 1.76,
            "text": "And there are others like me.",
        },
        {
            "start": 272.44,
            "end": 276.7,
            "duration": 4.26,
            "text": "I know you'll want to know what it's like there but honestly you wouldn't understand.",
        },
        {"start": 278.4, "end": 278.9, "duration": 0.5, "text": "Oh.."},
        {
            "start": 279.2,
            "end": 280.78,
            "duration": 1.58,
            "text": "You said, a little let down.",
        },
        {
            "start": 281.92,
            "end": 282.46000000000004,
            "duration": 0.54,
            "text": "But wait..",
        },
        {
            "start": 283.24,
            "end": 289.22,
            "duration": 5.98,
            "text": "If I get reincarnated to other places in time, I could have interacted with myself at some point.",
        },
        {
            "start": 291.0,
            "end": 292.74,
            "duration": 1.74,
            "text": "Sure, happens all the time.",
        },
        {
            "start": 293.24,
            "end": 298.72,
            "duration": 5.48,
            "text": "And with both lives only aware of their own lifespans, you don't even know it's happening.",
        },
        {
            "start": 356.56,
            "end": 359.12,
            "duration": 2.56,
            "text": "or who will ever live,  yes",
        },
        {
            "start": 359.7,
            "end": 360.96,
            "duration": 1.26,
            "text": "I'm Abraham Lincoln?",
        },
        {
            "start": 361.78,
            "end": 363.96,
            "duration": 2.18,
            "text": "and your john wilks booth too? (i didn't get what he said)",
        },
        {
            "start": 364.6,
            "end": 365.78000000000003,
            "duration": 1.18,
            "text": "I'm Hitler!!!",
        },
        {
            "start": 366.78,
            "end": 368.21999999999997,
            "duration": 1.44,
            "text": "You said appalled",
        },
        {
            "start": 368.8,
            "end": 370.88,
            "duration": 2.08,
            "text": "And you're the millions he killed.",
        },
        {"start": 371.36, "end": 372.88, "duration": 1.52, "text": "I'm Jesus!"},
        {
            "start": 373.2,
            "end": 375.18,
            "duration": 1.98,
            "text": "and you're everyone who followed Him.",
        },
        {"start": 376.06, "end": 377.26, "duration": 1.2, "text": "You fell silent*"},
        {
            "start": 378.44,
            "end": 381.86,
            "duration": 3.42,
            "text": "Every time you victimizing someone you're victimizing myself",
        },
        {
            "start": 382.74,
            "end": 386.24,
            "duration": 3.5,
            "text": "every act of kindness you've done you've done to yourself",
        },
        {
            "start": 387.02,
            "end": 394.47999999999996,
            "duration": 7.46,
            "text": "every happy and sad moment ever experienced by any human was or will be experienced by YOU",
        },
        {
            "start": 396.1,
            "end": 397.48,
            "duration": 1.38,
            "text": "you thought for a long time",
        },
        {
            "start": 398.98,
            "end": 402.32,
            "duration": 3.34,
            "text": "why?  why do all this?",
        },
        {
            "start": 402.62,
            "end": 405.3,
            "duration": 2.68,
            "text": "because someday you will become like me",
        },
        {
            "start": 405.9,
            "end": 407.28,
            "duration": 1.38,
            "text": "because that's what you are!",
        },
        {
            "start": 408.14,
            "end": 410.2,
            "duration": 2.06,
            "text": "you're one of my kind",
        },
        {"start": 410.32, "end": 412.58, "duration": 2.26, "text": "You're my child!"},
        {
            "start": 413.26,
            "end": 415.12,
            "duration": 1.86,
            "text": "Wow!! you said incredulous..",
        },
        {
            "start": 415.82,
            "end": 417.26,
            "duration": 1.44,
            "text": "you mean i'm a God?",
        },
        {
            "start": 419.02,
            "end": 421.5,
            "duration": 2.48,
            "text": "No, not yet, you're a fetus",
        },
        {
            "start": 421.7,
            "end": 422.97999999999996,
            "duration": 1.28,
            "text": "you're still growing.",
        },
        {
            "start": 423.14,
            "end": 426.62,
            "duration": 3.48,
            "text": "once you've lived every human life throughout all time",
        },
        {
            "start": 427.2,
            "end": 429.32,
            "duration": 2.12,
            "text": "you will have grown enough to be born",
        },
        {
            "start": 431.14,
            "end": 435.71999999999997,
            "duration": 4.58,
            "text": "so the whole universe... it's just... an egg",
        },
        {
            "start": 436.58,
            "end": 437.85999999999996,
            "duration": 1.28,
            "text": "I answered..",
        },
        {
            "start": 438.12,
            "end": 443.06,
            "duration": 4.94,
            "text": "now it's time for you to move on to your next life and I sent you on your way (this is the final clip of this video, made by Kurzgesagt subscribe to him!!!)",
        },
    ]
