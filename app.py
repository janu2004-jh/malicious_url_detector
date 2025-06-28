# app.py
from flask import Flask, render_template, request
import pandas as pd
import re
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

import difflib

popular_brands = [
    'google', 'facebook', 'instagram', 'youtube', 'twitter',
    'linkedin', 'amazon', 'netflix', 'microsoft', 'apple',
    'swiggy', 'zomato', 'paytm', 'flipkart', 'snapdeal',
    'ola', 'uber', 'airtel', 'jio', 'hdfc', 'icici', 'sbi', 'axis'
]


def looks_like_brand(url):
    domain = re.sub(r'https?://(www\.)?', '', url).split('/')[0].lower()
    for brand in popular_brands:
        similarity = difflib.SequenceMatcher(None, domain, brand).ratio()
        if similarity > 0.7 and brand not in domain:
            return 1  # Suspicious similarity
    return 0

def extract_features(url):
    return {
        'url_length': len(url),
        'digit_count': sum(c.isdigit() for c in url),
        'has_https': int(url.startswith("https")),
        'has_ip': int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url))),
        'count_special': sum(c in url for c in ['@', '-', '_', '%', '&', '=']),
        'suspicious_words': int(any(w in url.lower() for w in ['login', 'secure', 'update', 'bank', 'verify'])),
        'fake_brand': looks_like_brand(url),
    }


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    url = ""
    if request.method == "POST":
        url = request.form.get("url")
        features = pd.DataFrame([extract_features(url)])
        prediction = model.predict(features)[0]
        result = "Malicious" if prediction == 1 else "Benign"
    return render_template("index.html", result=result, url=url)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

