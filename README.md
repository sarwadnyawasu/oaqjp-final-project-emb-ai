# oaqjp-final-project-emb-ai# oaqjp-final-project-emb-ai

## Emotion Detection Application

This project is the final project for the IBM AI Application with Python course. It builds an Emotion Detection application using the Watson NLP library (via the Watson NLP Embed API). The application is deployed as a web application using Flask.

## Project Name
**Emotion Detection App** – An AI-powered web application that analyzes text input and detects emotional content including anger, disgust, fear, joy, and sadness, returning the dominant emotion.

## Features
- Detects five emotions: anger, disgust, fear, joy, sadness
- Returns emotion scores and the dominant emotion
- Handles blank/invalid input gracefully (error handling)
- Deployed as a Flask web application
- Static code analysis with pylint

## Technologies Used
- Python 3
- Watson NLP Embed API (via `requests`)
- Flask (web framework)
- Pylint (static analysis)
- unittest (unit testing)

## Project Structure
```
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── README.md
```

## How to Run
1. Start the Watson NLP Embed container locally on port 8080
2. Install dependencies: `pip install flask requests`
3. Run: `python server.py`
4. Visit: `http://localhost:5000`
