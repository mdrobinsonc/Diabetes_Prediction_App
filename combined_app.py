import streamlit as st
import joblib
import numpy as np
from PIL import Image

# Streamlit UI Configuration
st.set_page_config(page_title='Diabetes Prediction App', page_icon='�힙', layout='centered', initial_sidebar_state='expanded')

# Title and Description with Styling
st.markdown("""
    <style>
    .main-title {
        font-size: 48px;
        color: #1f77b4;
        text-align: center;
        font-weight: bold;
    }
    .description {
        font-size: 18px;
        text-align: center;
        color: #4b4b4b;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Diabetes Prediction App �힙</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Enter the required details below to check if you are at risk for diabetes. 💉</div>', unsafe_allow_html=True)

# Display a header image
header_image = 'diabetesimage.jpeg'
st.image(header_image, use_container_width=True)

# Sidebar for Model Selection
st.sidebar.markdown("""
    <style>
    .sidebar-title {
        font-size: 24px;
        color: #1f77b4;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown('<div class="sidebar-title">Choose Model & Input Your Health Information</div>', unsafe_allow_html=True)

# Model selection
model_choice = st.sidebar.radio(
    "Select the model:",
    ('Model with Selected Features', 'Model with All Features')
)

# Load the chosen model
if model_choice == 'Model with Selected Features':
    model = joblib.load('diabetes_model_selected_features.joblib')
    
    # Input fields for selected features
    Pregnancies = st.sidebar.slider('Number of Pregnancies', min_value=0, max_value=20, value=0)
    Glucose = st.sidebar.slider('Glucose Level', min_value=0, max_value=200, value=100)
    SkinThickness = st.sidebar.slider('Skin Thickness (mm)', min_value=0, max_value=99, value=20)
    BMI = st.sidebar.slider('BMI (Body Mass Index)', min_value=0.0, max_value=70.0, value=25.0, format="%.1f")
    DiabetesPedigreeFunction = st.sidebar.slider('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.5, format="%.2f")
    Age = st.sidebar.slider('Age', min_value=0, max_value=100, value=30)
    
    input_data = np.array([[Pregnancies, Glucose, SkinThickness, BMI, DiabetesPedigreeFunction, Age]])

else:
    model = joblib.load('diabetes_model_all_features.joblib')
    
    # Input fields for all features
    Pregnancies = st.sidebar.slider('Number of Pregnancies', min_value=0, max_value=20, value=0)
    Glucose = st.sidebar.slider('Glucose Level', min_value=0, max_value=200, value=100)
    BloodPressure = st.sidebar.slider('Blood Pressure (mmHg)', min_value=0, max_value=200, value=120)
    SkinThickness = st.sidebar.slider('Skin Thickness (mm)', min_value=0, max_value=99, value=20)
    Insulin = st.sidebar.slider('Insulin', min_value=0, max_value=300, value=60)
    BMI = st.sidebar.slider('BMI (Body Mass Index)', min_value=0.0, max_value=70.0, value=25.0, format="%.1f")
    DiabetesPedigreeFunction = st.sidebar.slider('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.5, format="%.2f")
    Age = st.sidebar.slider('Age', min_value=0, max_value=100, value=30)

    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

# Predict button styling
st.markdown("""
    <style>
    .predict-button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #135e96;
    }
    </style>
""", unsafe_allow_html=True)

# Predict button
if st.button('Predict ▶️'):
    prediction = model.predict(input_data)
    
    # Display result
    if prediction[0] == 1:
        st.markdown('<div class="main-title" style="color: red;">You are likely to have diabetes.</div>', unsafe_allow_html=True)
        st.image('OMH-diabets.gif', use_container_width=True)
        st.warning('Please consult a healthcare professional.')
    else:
        st.markdown('<div class="main-title" style="color: green;">You are unlikely to have diabetes.</div>', unsafe_allow_html=True)
        st.image('health.gif', use_container_width=True)
        st.balloons()
        st.success('Stay healthy! 🌿')

# Footer with developer credits
st.markdown("""
    <style>
    .footer {
        text-align: center;
        font-size: 14px;
        color: #4b4b4b;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="footer">Developed by Group1</div>', unsafe_allow_html=True)