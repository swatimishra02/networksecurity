import joblib
import pandas as pd

# Load preprocessor and model
preprocessor = joblib.load("final_model/preprocessor.pkl")
model = joblib.load("final_model/model.pkl")

# Check the feature names the preprocessor expects
# if hasattr(preprocessor, "feature_names_in_"):
#     print("Feature names during training (from preprocessor):", preprocessor.feature_names_in_)
# else:
#     print("Preprocessor does not have feature_names_in_ attribute.")

# # Check if the model has saved feature names (if applicable)
# if hasattr(model, "feature_names_in_"):
#     print("Feature names during training (from model):", model.feature_names_in_)
# else:
#     print("Model does not have feature_names_in_ attribute.")

# Training features
df = pd.read_csv(r"valid_data\test.csv")
training_features = set(preprocessor.feature_names_in_)  # From Step 1
# Prediction features
prediction_features = set(df.columns)

# Identify mismatches
missing_in_prediction = training_features - prediction_features
unseen_in_training = prediction_features - training_features

print("Features expected by the model but missing in prediction data:", missing_in_prediction)
print("Features in prediction data but unseen during training:", unseen_in_training)

