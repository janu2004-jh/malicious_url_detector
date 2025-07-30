 malicious_url_detector deployed in Render cloud 
"https://phish-shield.onrender.com"

🚨 Malicious URL Detector 🔗

An intelligent web-based system that detects and classifies URLs as malicious or benign using machine learning. Built with Python (Flask), trained on a real dataset, and deployed seamlessly on Render.

📌 Overview

With the exponential growth of phishing attacks and online scams, it's crucial to have an automated system to detect malicious URLs before they cause harm. This project leverages machine learning to classify URLs as safe or dangerous in real-time.


🧠 Features

✅ Real-Time URL Prediction

📊 Confidence Score Display

⚠️ Detects phishing, IP-based URLs, and suspicious patterns

📈 Trained on real-world datasets (malicious vs benign URLs)

🌐 Deployed on Render for public access

💬 Simple, interactive user interface for input & result display


🏗️ Tech Stack

Component	Tech Used

Backend	Python, Flask
ML Model	Logistic Regression / Random Forest (Scikit-learn)
Dataset	Open-source malicious URL dataset (CSV)
Frontend	HTML, CSS (Bootstrap)
Deployment	Render.com


🚀 How It Works

1. 🧹 Preprocessing:
Extracts lexical features (length, digits, special characters, etc.) from the given URL.


2. 🤖 ML Model:
Trained on labeled dataset with features like:

Use of IP in URL

Presence of @, -, //

Length, subdomain count

Blacklisted words like login, verify, update, etc.


3. 📈 Prediction:
Classifies the URL with a probability/confidence score using the trained model.


4. 💻 Output:
Returns either:

🚫 Malicious URL — Dangerous to Click!
✅ Safe URL — No immediate threat detected.


🧠 Future Enhancements

Add support for live web scraping of URLs for deeper analysis

Incorporate deep learning models (like RNNs for sequence-based URL detection)

Create browser extension version

Log predictions for admin monitoring



