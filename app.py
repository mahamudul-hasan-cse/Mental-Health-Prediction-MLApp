import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_resource
def load_model():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

def main():
    st.title("Mental Health Risk Prediction")

    age = st.slider("Age", 10, 100, 25)
    stress = st.slider("Stress Level (1-10)", 1, 10, 5)
    sleep = st.slider("Sleep Hours", 0, 24, 7)
    anxiety = st.slider("Anxiety Score (1-10)", 1, 10, 5)

    if st.button("Predict"):
        model, scaler = load_model()
        data = np.array([[age, stress, sleep, anxiety]])
        scaled_data = scaler.transform(data)
        result = model.predict(scaled_data)[0]
        st.success(f"Mental Health Risk Prediction: {result}")

if __name__ == "__main__":
    main()
