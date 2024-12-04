from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def website():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    #text = "I love my life"
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)
    if not result['dominant_emotion']:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}.")

if __name__ == '__main__':
    app.run(debug=True)
