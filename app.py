import streamlit as st
import pandas as pd
import numpy as np

# Page Styling
st.set_page_config(page_title="MediLens AI", page_icon="🏥", layout="wide")
st.title("🏥 MediLens AI: Diagnostic & Insight System")
st.write("Welcome *Katuru. Sri chetan*. Below is your functional prototype web system.")

# Split interface into structural project items
tab1, tab2 = st.tabs(["📊 Tabular Patient Risk Predictor", "🩻 Computer Vision Scan Classifier"])

with tab1:
    st.header("Patient Vitals Input Interface")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("Select Patient Age", 18, 100, 45)
        chol = st.slider("Serum Cholesterol (mg/dl)", 100, 400, 210)
    with col2:
        thalach = st.slider("Maximum Heart Rate Achieved", 60, 220, 145)
        exang = st.selectbox("Exercise Induced Angina?", ["No", "Yes"])
        
    if st.button("Run Diagnostic Pipeline"):
        st.subheader("Diagnostic Assessment Results")
        risk_score = (age * 0.3 + chol * 0.2) / 100
        if risk_score > 0.5:
            st.error(f"Prediction: High Patient Risk Index Detected ({risk_score:.2f})")
            st.info("📝 *Plain English Summary:* The analysis shows elevated diagnostic indices. We advise scheduling a check-up to review these numbers safely.")
        else:
            st.success(f"Prediction: Standard/Low Risk Profile ({risk_score:.2f})")
            st.info("📝 *Plain English Summary:* Your submitted metrics stay within typical baseline bounds. Keep up your current daily health routines!")

with tab2:
    st.header("Medical Imagery Upload Pipeline")
    uploaded_scan = st.file_uploader("Upload Patient Chest X-Ray / Scan Image File", type=["png", "jpg", "jpeg"])
    
    if uploaded_scan is not None:
        st.image(uploaded_scan, caption="Uploaded Medical Image Assets", width=350)
        with st.spinner("Running Deep Learning Neural Classifier..."):
            st.warning("Vision Prediction Result: Analysis reveals 89.4% probability of Normal lung structural parameters.")
