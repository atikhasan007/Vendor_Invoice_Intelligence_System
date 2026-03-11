import joblib
import pandas as pd

MODEL_PATH = "invoice_flagging/models/predict_flag_invoice.pkl"
SCALER_PATH = "invoice_flagging/models/scaler.pkl"

FEATURES = [
    "invoice_quantity",
    "invoice_dollars",
    "Freight",
    "total_item_quantity",
    "total_item_dollars"
]

def load_model():
    """Load invoice flagging model and scaler"""
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return model, scaler

def predict_invoice_flag(input_data):
    """Predict if invoice should be flagged"""
    model, scaler = load_model()
    input_df = pd.DataFrame(input_data)

    # Ensure feature order same as training
    input_df = input_df[FEATURES]

    # Scale features
    input_scaled = scaler.transform(input_df)

    preds = model.predict(input_scaled)
    input_df["Predicted_Flag"] = preds
    return input_df

# Optional: test run
if __name__ == "__main__":
    sample_data = {
        "invoice_quantity": [100, 80],
        "invoice_dollars": [18500, 9000],
        "Freight": [500, 300],
        "total_item_quantity": [110, 85],
        "total_item_dollars": [18400, 8900]
    }
    prediction = predict_invoice_flag(sample_data)
    print(prediction)
