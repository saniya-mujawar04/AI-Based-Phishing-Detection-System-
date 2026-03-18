from flask import Flask, render_template, request
from predict import predict_url
import csv
import os
import pandas as pd

app = Flask(__name__)

LOG_FILE = "logs.csv"


# -------------------------------
# Create logs file if not exists
# -------------------------------
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["url", "result", "risk"])


# -------------------------------
# Save log function
# -------------------------------
def save_log(url, result, risk):
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([url, result, risk])


# -------------------------------
# Home Route
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    risk = None

    if request.method == "POST":
        url = request.form["url"]

        result, risk = predict_url(url)

        # save into logs.csv
        save_log(url, result, risk)

    return render_template("index.html", result=result, risk=risk)


# -------------------------------
# Dashboard Route
# -------------------------------
@app.route("/dashboard")
def dashboard():
    df = pd.read_csv(LOG_FILE)

    total = len(df)
    phishing = len(df[df["result"] == "Phishing"])
    safe = len(df[df["result"] == "Safe"])
    avg_risk = round(df["risk"].mean(), 2) if total > 0 else 0

    recent = df.tail(5).values.tolist()

    return render_template(
        "dashboard.html",
        total=total,
        phishing=phishing,
        safe=safe,
        avg_risk=avg_risk,
        recent=recent
    )


if __name__ == "__main__":
    app.run(debug=True)