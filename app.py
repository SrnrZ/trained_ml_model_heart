import streamlit as st
from predict_function import predict

st.title("Input Health Variables")

# Define the initial example_input dictionary for default values
example_input = {
    'HighBP': 0,
    'HighChol': 0,
    'CholCheck': 0,
    'BMI': 25,
    'Smoker': 0,
    'Stroke': 0,
    'Diabetes': 0,
    'PhysActivity': 0,
    'Fruits': 0,
    'Veggies': 0,
    'HvyAlcoholConsump': 0,
    'AnyHealthcare': 0,
    'NoDocbcCost': 0,
    'GenHlth': 3,
    'MentHlth': 0,
    'PhysHlth': 0,
    'DiffWalk': 0,
    'Sex': 0,
    'Age': 7,
    'Education': 3,
    'Income': 4
}

# Create a form for the user input fields
with st.form("health_form"):
    HighBP = st.selectbox('High Blood Pressure', [0, 1], index=example_input['HighBP'])
    HighChol = st.selectbox('High Cholesterol', [0, 1], index=example_input['HighChol'])
    CholCheck = st.selectbox('Cholesterol Check', [0, 1], index=example_input['CholCheck'])
    BMIndex = st.number_input('BMI', min_value=0, max_value=300, value=int(example_input['BMI']))
    Smoker = st.selectbox('Smoker', [0, 1], index=example_input['Smoker'])
    Stroke = st.selectbox('Stroke', [0, 1], index=example_input['Stroke'])
    Diabetes = st.selectbox('Diabetes', [0, 1, 2], index=example_input['Diabetes'])
    PhysActivity = st.selectbox('Physical Activity', [0, 1], index=example_input['PhysActivity'])
    Fruits = st.selectbox('Fruits', [0, 1], index=example_input['Fruits'])
    Veggies = st.selectbox('Veggies', [0, 1], index=example_input['Veggies'])
    HvyAlcoholConsump = st.selectbox('Heavy Alcohol Consumption', [0, 1], index=example_input['HvyAlcoholConsump'])
    AnyHealthcare = st.selectbox('Any Healthcare', [0, 1], index=example_input['AnyHealthcare'])
    NoDocbcCost = st.selectbox('No Doctor because of Cost', [0, 1], index=example_input['NoDocbcCost'])
    GenHlth = st.slider('General Health (1-5)', min_value=1, max_value=5, value=example_input['GenHlth'])
    MentHlth = st.number_input('Mental Health Days', min_value=0, max_value=30, value=int(example_input['MentHlth']))
    PhysHlth = st.number_input('Physical Health Days', min_value=0, max_value=30, value=int(example_input['PhysHlth']))
    DiffWalk = st.selectbox('Difficulty Walking', [0, 1], index=example_input['DiffWalk'])
    Sex = st.selectbox('Sex (0=Female, 1=Male)', [0, 1], index=example_input['Sex'])
    Age = st.slider('Age Group (1-13)', min_value=1, max_value=13, value=example_input['Age'])
    Education = st.slider('Education Level (1-6)', min_value=1, max_value=6, value=example_input['Education'])
    Income = st.slider('Income Level (1-8)', min_value=1, max_value=8, value=example_input['Income'])

    # Add a submit button for the form
    submitted = st.form_submit_button("Confirm")

# If the confirm button is clicked, update example_input and display the prediction
if submitted:
    # Update the example_input dictionary with new values
    example_input.update({
        'HighBP': HighBP,
        'HighChol': HighChol,
        'CholCheck': CholCheck,
        'BMI': BMIndex,
        'Smoker': Smoker,
        'Stroke': Stroke,
        'Diabetes': Diabetes,
        'PhysActivity': PhysActivity,
        'Fruits': Fruits,
        'Veggies': Veggies,
        'HvyAlcoholConsump': HvyAlcoholConsump,
        'AnyHealthcare': AnyHealthcare,
        'NoDocbcCost': NoDocbcCost,
        'GenHlth': GenHlth,
        'MentHlth': MentHlth,
        'PhysHlth': PhysHlth,
        'DiffWalk': DiffWalk,
        'Sex': Sex,
        'Age': Age,
        'Education': Education,
        'Income': Income
    })

    # Call the predict function with updated example_input
    example_output = predict(example_input)
    st.write("Estimation:", example_output)