# app.py
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="AI Student Math Score Predictor",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>

/* Predict Button */
.stButton > button {
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    border: none;
    height: 3.2em;
    font-size: 18px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
    box-shadow: 0px 4px 12px rgba(37,99,235,0.35);
}

/* Footer */
.footer {
    text-align: center;
    color: #6B7280;
    font-size: 15px;
    padding-top: 10px;
}

</style>
""", unsafe_allow_html=True)

#loaded_model = joblib.load("Student_Math_Score_prediction.pkl")
loaded_model = None
#st.write(type(loaded_model))

with st.sidebar:

    st.header("Project Information")

    st.write("**Developer**")
    st.write("Ahmed Nawaz")

    st.write("**Machine Learning Model**")
    st.write("Linear Regression")

    st.write("**Instructor**")
    st.write("Sir Zafar Iqbal")

    st.write("**Version**")
    st.write("1.0")

    st.write("**Year**")
    st.write("2026")

st.title("🎓 Student Math Score Predictor")

st.info(
    """
 **Machine Learning Powered Prediction System**

Enter the student's academic details below and click **Predict Math Score**
to estimate the Mathematics score using our trained Linear Regression model.
"""
)

st.divider()


st.subheader(" Student Information")
st.caption("Please provide the student's details below.")


col1,col2 = st.columns(2)

with col1:
    reading = st.number_input(" Reading Score",0,100,50,help="Enter the student's Reading Exam Score (0–100).")
    gender = st.selectbox(" Gender",["Male","Female"],help="Select the student's gender.")
    race = st.selectbox(" Race / Ethnicity",
        ["Group A","Group B","Group C","Group D","Group E"],help="Select the student's race or ethnicity.")

with col2:
    writing = st.number_input(" Writing Score",0,100,50,help="Enter the student's Writing Exam Score (0–100).")
    lunch = st.selectbox(" Lunch Type",["Standard","Free/Reduced"],help="Select the student's lunch program.")
    test = st.selectbox(" Test Preparation",["Completed","None"],help="Select the student's test preparation status.")

parent = st.selectbox(
    " Parent Education",
    ["Associate's Degree","Bachelor's Degree","High School",
     "Master's Degree","Some College","Some High School"],help="Select the highest education level of the student's parent.")


gender_male = 1 if gender=="Male" else 0
lunch_standard = 1 if lunch=="Standard" else 0
test_none = 1 if test=="None" else 0

parent_bachelor=parent_high_school=parent_master=0
parent_some_college=parent_some_high_school=0
if parent=="Bachelor's Degree":
    parent_bachelor=1
elif parent=="High School":
    parent_high_school=1
elif parent=="Master's Degree":
    parent_master=1
elif parent=="Some College":
    parent_some_college=1
elif parent=="Some High School":
    parent_some_high_school=1

race_B=race_C=race_D=race_E=0
if race=="Group B":
    race_B=1
elif race=="Group C":
    race_C=1
elif race=="Group D":
    race_D=1
elif race=="Group E":
    race_E=1

new_student=pd.DataFrame({
"reading score":[reading],
"writing score":[writing],
"gender_male":[gender_male],
"lunch_standard":[lunch_standard],
"test preparation course_none":[test_none],
"parental level of education_bachelor's degree":[parent_bachelor],
"parental level of education_high school":[parent_high_school],
"parental level of education_master's degree":[parent_master],
"parental level of education_some college":[parent_some_college],
"parental level of education_some high school":[parent_some_high_school],
"race/ethnicity_group B":[race_B],
"race/ethnicity_group C":[race_C],
"race/ethnicity_group D":[race_D],
"race/ethnicity_group E":[race_E]
})

# ==========================================
# Prediction Section
# ==========================================

st.divider()

if st.button(" Predict Math Score", use_container_width=True):
    st.info("Debug Mode")
    st.stop()

    # Arrange columns according to trained model
    new_student = new_student.reindex(
        columns=loaded_model.feature_names_in_
    )

    # Predict Math Score
    prediction = loaded_model.predict(new_student)[0]

    # ==========================================
    # Grade System
    # ==========================================

    if prediction >= 90:
        grade = "A+"
        status = "Outstanding "

    elif prediction >= 80:
        grade = "A"
        status = "Excellent "

    elif prediction >= 70:
        grade = "B"
        status = "Good "

    elif prediction >= 60:
        grade = "C"
        status = "Average "

    else:
        grade = "D"
        status = "Needs Improvement "

    # ==========================================
    # Result Dashboard
    # ==========================================

    st.divider()

    st.subheader(" Prediction Dashboard")
    st.caption("Prediction generated using the trained Machine Learning model.")

    st.markdown("## 🎯 Prediction Result")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label=" Math Score",
            value=f"{prediction:.2f}"
        )

    with col2:
        st.metric(
            label=" Grade",
            value=grade
        )

    with col3:
        st.metric(
            label=" Performance",
            value=status
        )

    # ==========================================
    # Progress Bar
    # ==========================================

    st.progress(int(prediction))

    st.caption(f"Overall Estimated Performance: {prediction:.0f}%")

    # ==========================================
    # Performance Message
    # ==========================================

    if prediction >= 90:
        st.success(" Outstanding! The student is expected to achieve an excellent Mathematics score.")

    elif prediction >= 80:
        st.success(" Excellent! Strong academic performance predicted.")

    elif prediction >= 70:
        st.info(" Good! The predicted Mathematics score is above average.")

    elif prediction >= 60:
        st.warning(" Average performance. There is room for improvement.")

    else:
        st.error(" Improvement recommended. Additional practice may help increase the Mathematics score.")

st.divider()

st.markdown("""
<div class="footer">
Developed by Ahmed Nawaz | Machine Learning Project 2026 | Powered by Streamlit & Scikit-learn
</div>
""", unsafe_allow_html=True)