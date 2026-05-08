import streamlit as st
import requests

url = "http://127.0.0.1:8000/predict"

st.title("🚗Vehicle Insurance Claim Fraud Detection")

#Suspicious_Report	Sex	MaritalStatus	RepNumber	Age	High_Risk_Individual	

st.write("Enter the details ")

Suspicious_Report = st.selectbox("Suspicious Report ", [0,1])
Sex = st.selectbox("Sex", ["Male", "Female"])
MaritalStatus = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widow"])
RepNumber = st.number_input("Rep Number", min_value=1, max_value=16)
Age = st.slider("Age", min_value=0, max_value=100)
High_Risk_Individual = st.selectbox("High Risk Individual", [0,1])

if st.button("Predict"):
    data = {
        "Suspicious_Report": Suspicious_Report,
        "Sex": Sex,
        "MaritalStatus": MaritalStatus,
        "RepNumber": RepNumber,
        "Age": Age,
        "High_Risk_Individual": High_Risk_Individual
    }
    response = requests.post(url, json=data)
    result = response.json()

    st.write("Prediction:", result['result'])
    st.write("Confidence:", result['confidence'])