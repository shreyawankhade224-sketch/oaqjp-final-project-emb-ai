"""Task 2 Initial Implementation: Watson NLP API call returning raw response text."""

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyze):
    """Send text to Watson NLP service and return raw response text."""
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, headers=HEADERS, json=payload, timeout=10)
    return response.text
