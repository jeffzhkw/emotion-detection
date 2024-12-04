import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    try:
        response = requests.post(url, headers=headers, json=input_json)
        if response.status_code ==  400:
            return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        response.raise_for_status()

        response_data = response.json()
        emotion_predictions = response_data.get('emotionPredictions')
        res_emotion = emotion_predictions[0].get('emotion')

        dominant_emotion_name = max(res_emotion, key=res_emotion.get)
        
        return_res = {
            'anger': res_emotion.get('anger'),
            'disgust': res_emotion.get('disgust'),
            'fear': res_emotion.get('fear'),
            'joy': res_emotion.get('joy'),
            'sadness': res_emotion.get('sadness'),
            'dominant_emotion': dominant_emotion_name
        }
        return return_res
    except requests.exceptions.RequestException as e:
        print(e)
