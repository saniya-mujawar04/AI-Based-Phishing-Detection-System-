import pickle
from features import extract_features

# load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


# -------------------------------
# Threat Calculation
# -------------------------------
def calculate_threat(url, model_proba):
    score = 0.0

    keywords = ["login", "verify", "bank", "secure", "account"]
    if any(word in url for word in keywords):
        score += 0.3

    if "@" in url:
        score += 0.2

    if len(url) > 60:
        score += 0.1

    score += model_proba * 0.4

    return min(score, 1.0)


# -------------------------------
# Vulnerability Calculation
# -------------------------------
def calculate_vulnerability(url):
    score = 0.0

    if url.startswith("https"):
        score += 0.2

    if len(url) < 50:
        score += 0.2

    brands = ["google", "amazon", "paypal", "sbi", "bank"]
    if any(b in url for b in brands):
        score += 0.4

    if url.count('.') <= 2:
        score += 0.2

    return min(score, 1.0)


# -------------------------------
# Main Prediction Function
# -------------------------------
def predict_url(url):
    url = url.lower().strip()

    features = extract_features(url)

    proba = model.predict_proba([features])[0][1]

    threat = calculate_threat(url, proba)
    vulnerability = calculate_vulnerability(url)

    risk = round(threat * vulnerability * 100, 2)

    result = "Phishing" if risk >= 40 else "Safe"

    return result, risk