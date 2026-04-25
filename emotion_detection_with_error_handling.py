"""
Emotion Detection module using Watson NLP Embed API.
Includes error handling for blank or invalid input (HTTP 400).
"""
import requests


def emotion_detector(text_to_analyse):
    """
    Detects emotions in the given text using the Watson NLP Embed API.
    Handles blank input by returning None values when a 400 status is received.

    Args:
        text_to_analyse (str): The text to analyse for emotions.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
              Returns None for all values if input is blank or invalid.
    """
    url = (
        'http://localhost:8080/v1/watson.runtime.nlp.v1/'
        'NlpService/EmotionPredict'
    )
    headers = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_json = response.json()

    emotions = response_json['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
