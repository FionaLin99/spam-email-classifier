import streamlit as st
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "logistic_regression.pkl")
vectorizer_path = os.path.join(BASE_DIR, "feature_extraction.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

st.set_page_config(page_title="Spam Email Classifier 🚀", page_icon="📧", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📧 Spam Email Classifier")
st.subheader("🤖 Enter your email content below, and I'll predict whether it's **Spam** or **Ham**!")

user_input = st.text_area("✉️ **Email Content:**", height=200)

if st.button("🚀 **Predict**"):
    if not user_input.strip():
        st.warning("⚠️ Please enter some text to classify.")
    else:
        input_features = vectorizer.transform([user_input])
        prediction = model.predict(input_features)

        if prediction[0] == 1:
            st.success("✅ This is a **HAM** email. Good to go! 📨")
        else:
            st.error("🚫 This is a **SPAM** email. Be careful! 🚨")

st.markdown("---")
st.markdown("📝 Created with ❤️ by **Fiona Lin**")
