import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("attrition_model.pkl","rb"))

st.title("Employee Attrition Prediction")

age = st.number_input("Age")
distance = st.number_input("Distance From Home")
income = st.number_input("Monthly Income")

if st.button("Predict Attrition"):

    input_data = np.array([[age, distance, income]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Employee likely to leave")
    else:
        st.success("Employee likely to stay")