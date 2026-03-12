import os
import tempfile
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import subprocess
import sys

app = Flask(__name__)

# Config
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
ALLOWED_EXTENSIONS = {'.exe', '.dll', '.sys'}

# Load model, scaler, encoders once at startup
MODEL_PATH   = "Model/rf_model.pkl"
SCALER_PATH  = "Model/scaler.pkl"
ENCODER_PATH = "Model/encoders.pkl"

rf_model      = joblib.load(MODEL_PATH)
scaler        = joblib.load(SCALER_PATH)
label_encoders = joblib.load(ENCODER_PATH)


def allowed_file(filename):
    ext = os.path.splitext(filename)[1].lower()
    return ext in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    # Validate file exists in request
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Only .exe, .dll, .sys allowed"}), 400

    # Read and check file size
    file_bytes = file.read()
    if len(file_bytes) > MAX_FILE_SIZE:
        return jsonify({"error": "File too large (max 50MB)"}), 400

    # Save to temp file for extractor
    suffix = os.path.splitext(file.filename)[1].lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    try:
        # Run extractor.py to get features CSV
        csv_output = tmp_path + ".csv"
        result = subprocess.run(
            [sys.executable, "extractor.py", tmp_path, csv_output],
            capture_output=True, text=True, timeout=30
        )

        if result.returncode != 0:
            return jsonify({"error": "Feature extraction failed", "detail": result.stderr}), 500

        # Load extracted features
        df_features = pd.read_csv(csv_output)

        # Drop non-feature columns if present
        for col in ["Name", "Malware"]:
            if col in df_features.columns:
                df_features.drop(col, axis=1, inplace=True)

        # Encode categorical columns
        for col in df_features.select_dtypes(include=["object"]).columns:
            if col in label_encoders:
                df_features[col] = df_features[col].map(
                    lambda x: label_encoders[col].transform([x])[0]
                    if x in label_encoders[col].classes_ else -1
                )

        # Scale
        df_scaled = pd.DataFrame(scaler.transform(df_features), columns=df_features.columns)

        # Predict
        prediction = rf_model.predict(df_scaled)[0]
        probability = rf_model.predict_proba(df_scaled)[0]

        label = "MALWARE" if prediction == 1 else "BENIGN"
        confidence = round(float(max(probability)) * 100, 2)

        # Top 5 important features for this file
        feat_imp = pd.Series(rf_model.feature_importances_, index=df_scaled.columns)
        top5 = feat_imp.nlargest(5).index.tolist()
        top5_values = {f: round(float(df_features[f].iloc[0]), 4) for f in top5}

        return jsonify({
            "filename": file.filename,
            "label": label,
            "confidence": confidence,
            "top_features": top5_values,
            "file_size_kb": round(len(file_bytes) / 1024, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        # Always clean up temp files
        for path in [tmp_path, tmp_path + ".csv"]:
            if os.path.exists(path):
                os.remove(path)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)