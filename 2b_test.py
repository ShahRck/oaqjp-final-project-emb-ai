"""Script to test emotion_detector import and basic functionality."""

from unittest.mock import patch, MagicMock
import json

# Simulate Watson NLP API response
mock_response_data = {
    "emotionPredictions": [
        {
            "emotion": {
                "anger": 0.006274985,
                "disgust": 0.0025598855,
                "fear": 0.009251528,
                "joy": 0.9680386,
                "sadness": 0.049744163
            }
        }
    ]
}

mock_response = MagicMock()
mock_response.status_code = 200
mock_response.json.return_value = mock_response_data

with patch('requests.post', return_value=mock_response):
    from EmotionDetection import emotion_detector
    result = emotion_detector("I am glad this happened")
    print(result)

