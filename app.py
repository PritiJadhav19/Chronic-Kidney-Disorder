# app.py

import streamlit as st
import numpy as np
import pickle

# Load the pre-trained model (make sure the model is saved as 'ckd_model.pkl')
# Use joblib or pickle to load your trained model for this purpose
# model = pickle.load(open('ckd_model.pkl', 'rb'))

st.title("Chronic Kidney Disorder Prediction")

st.write("""
This app predicts whether a person has Chronic Kidney Disorder (CKD) 
based on medical test inputs.
""")

# Function to make predictions
def predict_ckd(features):
    # Normally, we would use model.predict, but here it's simulated
    # prediction = model.predict([features])
    # For demonstration, let's assume a dummy prediction logic
    prediction = np.random.choice([0, 1])  # Replace this with model.predict([features])
    return "Positive for CKD" if prediction == 1 else "Negative for CKD"

# Input form for user to enter relevant data
with st.form("ckd_prediction_form"):
    st.subheader("Enter Patient Information")

    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=50, max_value=200, value=120)
    specific_gravity = st.number_input("Specific Gravity", min_value=1.000, max_value=1.030, value=1.015)
    albumin = st.number_input("Albumin Level", min_value=0, max_value=5, value=0)
    sugar = st.number_input("Sugar Level", min_value=0, max_value=5, value=0)
    red_blood_cells = st.selectbox("Red Blood Cells", ["Normal", "Abnormal"])
    
    # Translate categorical input to numerical (0 for Normal, 1 for Abnormal)
    red_blood_cells = 1 if red_blood_cells == "Abnormal" else 0

    # Create feature list for prediction
    features = [age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells]
    
    # Submit button
    submitted = st.form_submit_button("Predict")
    
    if submitted:
        # Make prediction and show result
        result = predict_ckd(features)
        st.success(f"Prediction: {result}")
