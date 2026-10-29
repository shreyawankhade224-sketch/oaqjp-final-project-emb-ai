# Emotion Detector

An emotion detection application using the IBM Watson NLP EmotionPredict
service, Python, and Flask.

## Features
- Detects anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion.
- Provides a Flask web interface and JSON endpoint.
- Handles blank and invalid input.
- Includes unit tests.

## Run
Install dependencies with `python -m pip install requests flask pylint`.
Run the tests with `python -m unittest test_emotion_detection.py`.
Start the web application with `python server.py`.
Open http://127.0.0.1:5000 in a browser.
