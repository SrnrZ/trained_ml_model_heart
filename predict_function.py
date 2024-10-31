import pandas as pd
import pickle

# Load the trained model and normalizer from model.py
with open('model.pkl', 'rb') as file:
    final_model = pickle.load(file)
with open('normalizer.pkl', 'rb') as file:
    normalizer = pickle.load(file)
with open('columns_to_normalize.pkl', 'rb') as file:
    columns_to_normalize = pickle.load(file)

def predict(input_data):
    """
    Make a prediction using the trained Random Forest model.
    
    Parameters:
    input_data (dict): A dictionary of health indicators.
    
    Returns:
    A dictionary containing the prediction, probability of heart disease, and the top contributing factors.
    """
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Normalize the input data
    input_norm = input_df.copy()
    input_norm[columns_to_normalize] = normalizer.transform(input_df[columns_to_normalize])
    
    # Make prediction
    prediction = final_model.predict(input_norm)[0]
    probability = final_model.predict_proba(input_norm)[0][1]
    
    # Get feature contributions
    feature_contributions = pd.DataFrame({
        'feature': input_df.columns,
        'contribution': final_model.feature_importances_ * abs(input_norm.iloc[0])
    }).sort_values('contribution', ascending=False)
    
    return {
        'prediction': 'High Risk' if prediction == 1 else 'Low Risk',
        'probability': probability,
        'top_factors': feature_contributions.head(10)
    }