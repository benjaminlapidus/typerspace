import pytest
import json

def test_api_response(
    mock_api_response,
    mock_api_get_video_transcript
):
    test_video_id = "h6fcK_fRYaI"
    api_response = json.loads(mock_api_get_video_transcript(test_video_id))
    assert api_response["id"] == test_video_id
    assert api_response["captions"] == mock_api_response