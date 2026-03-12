
import pandas as pd
import joblib
import sys
import os
import subprocess

LABELS = {0: "SAFE", 1: "MALWARE"}

def main():
    # ---------------- Parse arguments ----------------
    if len(sys.argv) != 2:
        sys.exit("Usage: python program.py [file_target.csv|file_target.exe|file_target.sys]")

    input_file = sys.argv[1]

    # ---------------- Load model and preprocessing ----------------
    model_file = "Model/rf_model.pkl"
    scaler_file = "Model/scaler.pkl"
    encoders_file = "Model/encoders.pkl"

    if not os.path.exists(model_file):
        sys.exit(f"[ERROR] Model file not found: {model_file}")

    print("[INFO] Loading model...")
    model = joblib.load(model_file)
    scaler = joblib.load(scaler_file) if os.path.exists(scaler_file) else None
    encoders = joblib.load(encoders_file) if os.path.exists(encoders_file) else None

    # ---------------- Handle PE files ----------------
    if input_file.lower().endswith((".exe", ".sys", ".dll")):
        workspace_dir = "Temp"
        os.makedirs(workspace_dir, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        csv_path = os.path.join(workspace_dir, f"{base_name}.csv")

        print(f"[INFO] Extracting features: {input_file} -> {csv_path}")
        try:
            subprocess.run(["python", "extractor.py", input_file, csv_path], check=True)
        except subprocess.CalledProcessError as e:
            sys.exit(f"[ERROR] Feature extraction failed: {e}")

        input_file = csv_path
        print("[INFO] Feature extraction completed.")

    # ---------------- Load dataset ----------------
    if not os.path.exists(input_file):
        sys.exit(f"[ERROR] Input file not found: {input_file}")

    print(f"[INFO] Loading dataset: {input_file}")
    data = pd.read_csv(input_file)
    X = data.drop(columns=["Malware"], errors="ignore")

    # ---------------- Apply encoders ----------------
    if encoders:
        print("[INFO] Applying encoders...")
        for col, le in encoders.items():
            if col in X.columns:
                X[col] = X[col].map(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

    # ---------------- Align features ----------------
    if hasattr(model, "feature_names_in_"):
        for col in model.feature_names_in_:
            if col not in X.columns:
                X[col] = 0
        X = X[model.feature_names_in_]

    # ---------------- Scale features ----------------
    if scaler:
        X = pd.DataFrame(scaler.transform(X), columns=X.columns)

    # ---------------- Predict ----------------
    print("[INFO] Running prediction...")
    preds = model.predict(X)

    print("[INFO] Prediction results:")
    for p in preds:
        print("  →", LABELS.get(p, str(p)))

if __name__ == "__main__":
    main()
