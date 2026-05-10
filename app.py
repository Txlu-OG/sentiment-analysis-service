from flask import Flask, request, jsonify
from model import predict_sentiment

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Sentiment Analysis Service - CI/CD Version!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    result = predict_sentiment(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)