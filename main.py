import streamlit as st
from prediction_helper import predict
import time

st.set_page_config(
    page_title="Health Insurance Premium Prediction",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add custom CSS for styling
st.markdown("""
    <style>
        /* Page background and font settings */
        body {
            background: linear-gradient(to bottom, #f0f8ff, #e0f7fa);
            font-family: 'Roboto', sans-serif;
            margin-top: -50px;
        }

        /* Title styling */
        h1 {
            text-align: center;
            background: linear-gradient(to left, #00bcd4, #00796b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3em;
            font-weight: bold;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.2);
            margin-bottom: 30px;
        }

        /* Subheading (h2) color styling */
        h2 {
            color: #00796b;  /* Set the subheading color to a shade of green */
            font-size: 1.8em;
            font-weight: 600;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        /* Label styling */
        label {
            color: #00796b;  /* Green color for the labels */
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 5px;
        }

        /* Input and select styling */
        .stNumberInput > div, .stSelectbox > div {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            padding: 5px;
            margin: 8px 0;
        }

        /* Button styling */
        .stButton > button {
            background: linear-gradient(to right, #4caf50, #8bc34a);
            color: white;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            padding: 15px 30px;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
        }

        .stButton > button:hover {
            background: linear-gradient(to right, #8bc34a, #4caf50);
            transform: scale(1.05);
        }

        /* Container styling for input sections */
        .input-container {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        /* Panel styling */
        .prediction-panel {
            background: rgba(255, 255, 255, 0.85);
            padding: 15px 25px;
            border-radius: 10px;
            font-size: 18px;
            color: #2e8b57;
            text-align: center;
        }

        /* Icon Styling */
        .icon {
            font-size: 24px;
            color: #00796b;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown("<h1>Insurance Premium Predictor</h1>", unsafe_allow_html=True)

# Input Fields Layout
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Personal Information Section
row1 = st.columns(3)
with row1[0]:
    age = st.number_input('👶 Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('👨‍👩‍👧 Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('💸 Income in Lakhs', step=1, min_value=0, max_value=200)

# Health and Employment Section
row2 = st.columns(3)
with row2[0]:
    genetical_risk = st.number_input('🧬 Genetical Risk', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('📋 Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('💼 Employment Status', categorical_options['Employment Status'])

# Demographics Section
row3 = st.columns(3)
with row3[0]:
    gender = st.selectbox('🚻 Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('💍 Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('⚖️ BMI Category', categorical_options['BMI Category'])

# Lifestyle Section
row4 = st.columns(3)
with row4[0]:
    smoking_status = st.selectbox('🚭 Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('📍 Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('🩺 Medical History', categorical_options['Medical History'])

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Button and Result in a Single Row (Horizontal layout)
row5 = st.columns([3, 5])  # Adjust column sizes to fit the layout

with row5[0]:
    if st.button('Predict'):
        # Show loading animation
        with st.spinner('Processing your data...'):
            time.sleep(2)  # Simulate a delay
            prediction = predict(input_dict)
    else:
        prediction = ""

with row5[1]:
    if prediction:
        st.markdown(f"""
            <div class="prediction-panel">
                Predicted Health Insurance Cost: <strong>{prediction}</strong>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Please fill in all fields correctly to make a prediction.")
