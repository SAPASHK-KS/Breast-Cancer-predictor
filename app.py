import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

st.set_page_config(
    page_title="Breast Cancer Predictor",
    layout="centered"
)

st.title("Breast Cancer Prediction App")
st.write("Logistic Regression Model")

st.divider()

radius = st.slider("Tumor Radius", 5.0, 30.0, 14.0)
texture = st.slider("Tumor Texture", 5.0, 40.0, 20.0)
smoothness = st.slider("Tumor Smoothness", 0.05, 0.20, 0.10)

st.divider()

if st.button("Predict"):
    input_df = pd.DataFrame(
        [[radius, texture, smoothness]],
        columns=features
    )

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error("Malignant Tumor Detected")
    else:
        st.success("Benign Tumor (Low Risk)")

    st.info(f"Prediction Confidence: {probability * 100:.2f}%")


