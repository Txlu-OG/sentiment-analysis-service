from transformers import pipeline

# Load pre-trained sentiment analysis model
classifier = pipeline("sentiment-analysis")

def predict_sentiment(text):
    result = classifier(text)[0]
    return {
        "label": result["label"],
        "confidence": float(result["score"])
    }