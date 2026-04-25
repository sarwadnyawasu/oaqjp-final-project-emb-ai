"""
Flask server for the Emotion Detection web application.
Provides a web interface and API endpoint for emotion analysis.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route to detect emotions from the text provided in query parameters.
    Handles blank input and returns formatted emotion analysis results.
    """
    text_to_analyse = request.args.get('textToAnalyse')

    if not text_to_analyse or text_to_analyse.strip() == "":
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant = result['dominant_emotion']

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return response_text


@app.route("/")
def render_index_page():
    """Render the main index page of the application."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
