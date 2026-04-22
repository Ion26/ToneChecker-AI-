from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive", polarity
    elif polarity < 0:
        return "Negative", polarity
    else:
        return "Neutral", polarity

def detect_emotion(text):
    text = text.lower()

    if any(word in text for word in ["happy", "great", "awesome", "good"]):
        return "Happy"
    elif any(word in text for word in ["sad", "bad", "down"]):
        return "Sad"
    elif any(word in text for word in ["angry", "hate", "annoyed"]):
        return "Angry"
    else:
        return "Neutral"

def generate_replies(sentiment):
    if sentiment == "Positive":
        return [
            "That's great to hear!",
            "Sounds awesome!",
            "Glad things are going well!"
        ]
    elif sentiment == "Negative":
        return [
            "I'm sorry to hear that.",
            "That sounds tough.",
            "Hope things get better soon."
        ]
    else:
        return [
            "Got it.",
            "Okay noted.",
            "Alright."
        ]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        text = request.form["text"]

        sentiment, polarity = analyze_sentiment(text)
        emotion = detect_emotion(text)
        replies = generate_replies(sentiment)

        result = {
            "text": text,
            "sentiment": sentiment,
            "polarity": round(polarity, 2),
            "emotion": emotion,
            "replies": replies
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)