# ToneChecker (AI)

## Overview
ToneChecker AI is a web-based application that analyzes user input text to detect sentiment and emotion, and generates smart replies based on the detected tone.

## Problem Statement
In digital communication, people often struggle to understand the tone of messages or respond appropriately. Misinterpretation can lead to confusion or conflict.

## Solution
ToneChecker AI uses Natural Language Processing (NLP) to:
- Detect sentiment (Positive, Negative, Neutral)
- Identify emotion (Happy, Sad, Angry)
- Generate context-aware replies

## Features
- Sentiment analysis using TextBlob
- Emotion detection using keyword-based logic
- AI-generated reply suggestions
- Simple and interactive web interface

## Tech Stack
- Python
- Flask
- TextBlob (NLP)
- HTML + CSS

## How to Run
1. Install dependencies:
   pip install flask textblob

2. Download required corpora:
   python -m textblob.download_corpora

3. Run the application:
   python app.py

4. Open browser and go to:
   http://127.0.0.1:5000

## Future Improvements
- Use advanced ML models for emotion detection
- Add voice input
- Improve UI/UX design
- Add real-time chat integration

##Author
Ayan Shams
25BHI10082