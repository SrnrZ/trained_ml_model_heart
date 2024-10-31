import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from imblearn.under_sampling import RandomUnderSampler
from sklearn.metrics import classification_report, confusion_matrix

# Load the data
data = pd.read_csv('C:/Users/Srnzzz/Documents/5- Ironhack/ML/heart_disease_health_indicators_BRFSS2015.csv', delimiter=';')

# 'HeartDiseaseorAttack' will be the target variable (y)
features = data.drop('HeartDiseaseorAttack', axis=1)
target = data['HeartDiseaseorAttack']

# Split the data initially
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 1: Identify columns with more than 2 unique values
columns_to_normalize = X_train.columns[X_train.nunique() > 2]

# Step 2: Normalize only those columns
normalizer = MinMaxScaler()
X_train_norm = X_train.copy()  # Make a copy to preserve original DataFrame
X_train_norm[columns_to_normalize] = normalizer.fit_transform(X_train[columns_to_normalize])

X_test_norm = X_test.copy()
X_test_norm[columns_to_normalize] = normalizer.transform(X_test[columns_to_normalize])

# Step 3: Apply Undersampling
undersampler = RandomUnderSampler(random_state=42)
X_train_resampled, y_train_resampled = undersampler.fit_resample(X_train_norm, y_train)

# Print class distribution before and after undersampling
print("Original class distribution:")
print(y_train.value_counts(normalize=True))
print("\nResampled class distribution:")
print(y_train_resampled.value_counts(normalize=True))

# Initialize Random Forest model
base_rf = RandomForestClassifier(random_state=42)

# Define hyperparameter search space
param_distributions = {
    'n_estimators': [100, 200, 300],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2']
}

# Perform randomized search for hyperparameter tuning
random_search = RandomizedSearchCV(
    base_rf, 
    param_distributions=param_distributions,
    n_iter=20,
    cv=5,
    random_state=42,
    n_jobs=-1,
    scoring='recall'  # Using recall as the evaluation metric
)

# Fit model on resampled data
random_search.fit(X_train_resampled, y_train_resampled)

# Get the best model
final_model = random_search.best_estimator_