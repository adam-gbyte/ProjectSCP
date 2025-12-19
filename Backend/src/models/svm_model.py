# Backend/src/model/svm_model.py
import joblib

scaler = joblib.load("models/scaler.pkl")
pca = joblib.load("models/pca.pkl")
svm_model = joblib.load("models/svm_model.pkl")

def predict_label(features):
    features_scaled = scaler.transform(features)
    features_pca = pca.transform(features_scaled)

    label = int(svm_model.predict(features_pca)[0])
    proba = svm_model.predict_proba(features_pca)[0]

    return {
        "label": label,
        "confidence": float(proba[label]),
        "probabilities": proba.tolist()
    }
