import joblib
import pandas as pd

MODEL_PATH = "freight_cost_prediction/models/predict_freight_model.pkl"
import joblib

MODEL_PATH = "freight_cost_prediction/models/predict_freight_model.pkl"

# Load the model
model = joblib.load(MODEL_PATH)

# Check features
print("Model expects these features:")
print(model.feature_names_in_)

def load_model(model_path: str = MODEL_PATH):
    """Load trained freight cost prediction model"""
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model

def predict_freight_cost(input_data):
    """Predict freight cost for new vendor invoices.

    Parameters
    ----------
    input_data: dict
        Dictionary with feature values

    Returns
    -------
    pd.DataFrame with predicted freight cost
    """
    model = load_model()
    input_df = pd.DataFrame(input_data)

    # Keep only features the model was trained with
    input_df = input_df[model.feature_names_in_]

    input_df['Predicted_Freight'] = model.predict(input_df).round()
    return input_df

# Optional: test run
if __name__ == "__main__":
    sample_data = {
        "Dollars": [18500, 9000, 3000, 200]
    }
    prediction = predict_freight_cost(sample_data)
    print(prediction)
