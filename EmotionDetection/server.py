from flask import Flask, request, jsonify
from emotion_detection import emotion_detector  # Import your emotion_detector function
app = Flask(__name__)
@app.route("/emotionDetector")
def emotion_detector_route():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    if response['status_code'] == 400:  # Handle None dominant emotion
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Extract the emotions and dominant emotion from the response
    anger = response['data']['anger']
    disgust = response['data']['disgust']
    fear = response['data']['fear']
    joy = response['data']['joy']
    sadness = response['data']['sadness']
    dominant_emotion = response['data']['dominant_emotion']

    # Return a formatted response
    return jsonify({
        "message": f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    }), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6000)
