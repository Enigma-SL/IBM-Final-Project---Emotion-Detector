"""
Flask server for Emotion Detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    API endpoint that receives text via query parameter 'textToAnalyze',
    returns the dominant emotion and its score in a formatted string.
    If text is empty or invalid, returns an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)
    return str(result)

@app.route("/")
def render_index_page():
    """Render the main HTML page (index.html)."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
