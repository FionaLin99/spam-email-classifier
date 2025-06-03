# 📧 Spam Email Classifier (Streamlit App)

This is a simple machine learning app that classifies email content as **Spam** or **Ham** using a Logistic Regression model.

## 🔍 How it works
- Trained on a dataset of labeled emails (`mail_data.csv`)
- Uses TF-IDF vectorization for feature extraction
- Predicts with a trained logistic regression model
- Interactive front-end built with Streamlit

## 📁 Project Structure
sideProject_spamEmail/
├── app.py # Streamlit app
├── logistic_regression.pkl # Trained ML model
├── feature_extraction.pkl # TF-IDF vectorizer
├── spam_email_classification.py # Training script 
├── mail_data.csv # Dataset
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 🛠 Tech Stack
- Python 3.7+
- scikit-learn
- pandas
- numpy
- Streamlit

## 🚀 Run locally
Make sure Python 3.7 or higher is installed. Then:

# 1. Navigate to the project folder
cd sideProject_spamEmail

# 2. Install the dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py

Streamlit will open the app in your browser automatically.
If not, visit: http://localhost:8501 (or the port shown in your terminal).

## Example Use
Paste an email's text into the input box and click "Predict".
The model will tell you if it’s likely Spam or Ham (not spam).


