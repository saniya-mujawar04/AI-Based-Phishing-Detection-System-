# AI-Based-Phishing-Detection-System-
Phishing detection system using AI and risk analysis with dashboard visualization

## Overview
This project is an AI-based phishing detection system that not only classifies URLs but also calculates risk using the concept:

Risk = Threat × Vulnerability

The system combines machine learning with rule-based analysis and provides a dashboard for visualization.

---

## Features
- URL classification using Machine Learning  
- Risk-based analysis instead of binary output  
- Rule-based threat detection (keywords, URL patterns)  
- Vulnerability assessment  
- Real-time logging using CSV  
- Dashboard with charts and recent activity  

---

## Tech Stack
- Python  
- Flask  
- Scikit-learn  
- Pandas  
- HTML, CSS  
- Chart.js  

---

## How It Works
1. User enters a URL  
2. Features are extracted from the URL  
3. ML model predicts probability  
4. Threat and Vulnerability scores are calculated  
5. Final Risk = Threat × Vulnerability  
6. Result is displayed and stored in logs  

---

# Project Structure
phishing_detection_system/
│
├── app.py
├── train_model.py
├── predict.py
├── features.py
├── phishing_dataset.csv
├── model.pkl
├── log.csv
├── clogs.csv
│
├── templates/
│ ├── index.html
│ └── dashboard.html
│
└── static/
└── style.css

##Project Output

### Home Page
! [Home Page] ("C:\Users\SANIYA\Downloads\pro1.png")

### Dashboard
![Dashboard]("C:\Users\SANIYA\Downloads\proj2.png")

## Future Improvements
- Improve dataset for better accuracy  
- Add advanced visual analytics  
- Deploy the system online  
- Integrate real-time phishing APIs  

## Author
Saniya Mujawar
