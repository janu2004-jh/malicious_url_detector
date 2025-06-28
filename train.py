import pandas as pd
import joblib
import re
import difflib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Brand list
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
        if similarity > 0.6 and brand not in domain:
            return 1
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

if __name__ == "__main__":
    df = pd.read_csv("dataset.csv")
    df.columns = [c.lower() for c in df.columns]
    df = df.rename(columns={"label": "target"})
    df["target"] = df["target"].map({"benign": 0, "malicious": 1})

    features = df["url"].apply(extract_features).apply(pd.Series)
    X, y = features, df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, max_depth=20, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"Model Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")

    joblib.dump(model, "model.pkl")
    print("✅ Model retrained and saved with improved brand spoofing detection.")
