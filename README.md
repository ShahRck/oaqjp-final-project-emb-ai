# Emotion Detector

A web application that detects emotions in text using Watson NLP.

## Description

This project uses the IBM Watson NLP Emotion Predict API to analyse text and identify the dominant emotion among five categories: anger, disgust, fear, joy, and sadness.

## Features

- Detects 5 emotions: anger, disgust, fear, joy, sadness
- Identifies the dominant emotion
- Web interface built with Flask
- Error handling for blank input
- Unit tested with Python unittest

## Project Structure

```
final_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── test_emotion_detection.py
├── server.py
└── README.md
```

## Usage

1. Install dependencies: `pip install flask requests`
2. Run the server: `python server.py`
3. Open browser at `http://localhost:5000`

## API

Uses Watson NLP Emotion Predict API:
- Endpoint: `https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict`
- Model: `emotion_aggregated-workflow_lang_en_stock`

