import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time
import plotly.graph_objects as go

# Load saved model and scaler
bundle = joblib.load("best_model_with_scaler.pkl")
model = bundle["model"]
scaler = bundle["scaler"]

# Title with style
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎓 Student Performance Predictor</h1>", unsafe_allow_html=True)
st.write("Fill in the details below and click **Predict** to see the final grade with an interactive visualization.")

# Sliders in main body
study_hours = st.slider("📖 Study Hours Per Day", 0.0, 11.7, 5.0)
attendance = st.slider("📊 Attendance Percentage", 45.2, 100.0, 75.0)
assignments = st.slider("📝 Assignments Completed", 0.0, 20.0, 10.0)
previous_marks = st.slider("📚 Previous Semester Marks", 24.7, 100.0, 70.0)
participation = st.slider("🙋 Class Participation", 1.0, 10.0, 5.0)

# Prediction button
if st.button("🔮 Predict Grade"):
    with st.spinner("Analyzing student performance..."):
        time.sleep(2)  # simulate loading animation

    # Prepare input
    input_data = pd.DataFrame([[study_hours, attendance, assignments, previous_marks, participation]],
                              columns=["Study_Hours_Per_Day", "Attendance_Percentage", 
                                       "Assignments_Completed", "Previous_Semester_Marks", 
                                       "Class_Participation"])
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]

    # Clip prediction to valid range (1–5)
    predicted_grade_num = int(round(np.clip(prediction, 1, 5)))

    # Map numeric prediction back to grade
    grade_map = {1: "A", 2: "B", 3: "C", 4: "D", 5: "F"}
    predicted_grade = grade_map[predicted_grade_num]

    # Show result with styled text
    st.markdown(f"<h2 style='text-align: center; color: #2196F3;'>📌 Predicted Grade: {predicted_grade}</h2>", unsafe_allow_html=True)

    # Attractive circular gauge chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=predicted_grade_num,
        title={'text': f"Final Grade ({predicted_grade})"},
        gauge={'axis': {'range': [1, 5], 'tickvals': [1,2,3,4,5], 'ticktext': ["A","B","C","D","F"]},
               'bar': {'color': "#4CAF50"},
               'steps': [
                   {'range': [1, 2], 'color': "#66BB6A"},
                   {'range': [2, 3], 'color': "#42A5F5"},
                   {'range': [3, 4], 'color': "#FFCA28"},
                   {'range': [4, 5], 'color': "#FF7043"}
                   ]}))

    st.plotly_chart(fig, width="stretch")

