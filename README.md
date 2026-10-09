AI Cyber Threat Detection and Intelligent Response

Project Overview

AI Cyber Threat Detection is a web application designed to identify potentially suspicious cyber activity. It analyzes login attempts, data transfer amounts, and unknown-device logins to help users recognize possible security risks.

Problem Statement

Small organizations and educational institutions may find it difficult to identify suspicious cyber activities quickly. This project provides a simple interface to analyze activity and highlight potential threats.

Key Features

- AI-based anomaly detection using Isolation Forest.
- Threat scoring out of 100.
- Risk level identification.
- Explanations of suspicious activities.
- Recommended security actions.
- Simple, interactive web interface.

Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib

How It Works

1. Enter cyber activity details.
2. The machine-learning model analyzes the activity.
3. The application displays the AI prediction.
4. A rule-based system calculates the threat score and risk level.
5. The application explains suspicious indicators and recommends an action.

How to Run

1. Install Python 3.13.

2. Install the required packages:
   
   "pip install streamlit pandas scikit-learn numpy joblib"

3. Train the model:
   
   "python train_model.py"

4. Start the application:
   
   "streamlit run app.py"

Limitations

This is a student prototype using sample training data and manually entered activity. It is not a replacement for professional cybersecurity monitoring. Predictions and threat scores should be verified before taking security action.

Responsible AI and Security

The system provides recommendations only. It does not automatically block devices or accounts. Do not enter real passwords, sensitive personal information, or confidential organizational data.

Project Purpose

To demonstrate how machine learning and explainable risk indicators can support basic cyber-threat awareness in educational and small-organization settings.
