import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from fastapi import FastAPI, UploadFile, File, HTTPException
import tempfile
import uuid
from pathlib import Path
from datetime import datetime
from bson import ObjectId

from src.models.mobilenet_model import extract_features
from src.models.svm_model import predict_label
from src.database.mongo import prediction_collection

app = FastAPI()

label_map = {
    0: "hampir_matang",
    1: "matang_sempurna",
    2: "mentah",
    3: "sangat_matang",
    4: "setengah_matang",
}

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "API is running..."
    }

# =========================
# POST : PREDICT + SAVE
# =========================
@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    # =========================
    # 1. SAVE IMAGE FILE
    # =========================
    ext = Path(file.filename).suffix  # .jpg / .png
    unique_name = f"{uuid.uuid4()}{ext}"

    year = datetime.utcnow().strftime("%Y")
    month = datetime.utcnow().strftime("%m")

    upload_dir = Path("uploads") / year / month
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / unique_name

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # =========================
    # 2. EXTRACT & PREDICT
    # =========================
    features = extract_features(str(file_path))
    result = predict_label(features)

    label = result["label"]
    confidence = result["confidence"]
    probabilities = result["probabilities"]

    prediction_text = label_map[label]

    # =========================
    # 3. SAVE TO MONGODB
    # =========================
    data = {
        "stored_filename": unique_name,
        "file_path": str(file_path),
        "label": label,
        "prediction": prediction_text,
        "confidence": confidence,
        "probabilities": probabilities,
        "created_at": datetime.utcnow()
    }

    inserted = prediction_collection.insert_one(data)

    return {
        "status": "success",
        "id": str(inserted.inserted_id),
        "prediction": prediction_text,
        "confidence": confidence,
        "image_path": str(file_path)
    }

@app.get("/predictions")
def get_predictions():
    cursor = prediction_collection.find().sort("created_at", -1)

    results = []
    for doc in cursor:
        doc["_id"] = str(doc["_id"])
        results.append(doc)

    return {
        "status": "success",
        "count": len(results),
        "data": results
    }

@app.get("/predictions/{prediction_id}")
def get_prediction_by_id(prediction_id: str):
    if not ObjectId.is_valid(prediction_id):
        raise HTTPException(status_code=400, detail="Invalid ID")

    doc = prediction_collection.find_one({"_id": ObjectId(prediction_id)})

    if not doc:
        raise HTTPException(status_code=404, detail="Data not found")

    doc["_id"] = str(doc["_id"])

    return {
        "status": "success",
        "data": doc
    }

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.staticfiles import StaticFiles

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")