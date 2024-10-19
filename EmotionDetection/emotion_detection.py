import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  # Check for blank input
        return {
            'status_code': 400,
            'data': {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send the request
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:  # Handle 400 Bad Request
        return {
            'status_code': 400,
            'data': {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        }

    # Convert response to JSON dictionary
    formatted_response = json.loads(response.text)

    # Extract emotions
    anger = formatted_response['emotion']['anger']
    disgust = formatted_response['emotion']['disgust']
    fear = formatted_response['emotion']['fear']
    joy = formatted_response['emotion']['joy']
    sadness = formatted_response['emotion']['sadness']

    # Determine the dominant emotion
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get) if any(emotion_scores.values()) else None

    return {
        'status_code': 200,
        'data': {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    }
