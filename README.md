# 🎗️ Breast Cancer Predictor

A Streamlit web app that predicts whether a breast tumor is **benign** or **malignant** using a Logistic Regression model trained on the Wisconsin Breast Cancer dataset.

> ⚠️ For educational purposes only. Not a medical diagnostic tool.

## Features

- Interactive sliders for tumor radius, texture, and smoothness
- Real-time prediction with confidence score
- Built with Streamlit + scikit-learn

## Project Structure

```
├── app.py                 # Streamlit app
├── model_training.ipynb   # Model training notebook
├── breast-cancer.csv      # Dataset
├── model.pkl              # Trained model
├── scaler.pkl             # Feature scaler
├── features.pkl           # Feature names
└── requirements.txt       # Dependencies
```

## Installation

```bash
git clone https://github.com/<your-username>/Breast-Cancer-predictor.git
cd Breast-Cancer-predictor
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

Open `http://localhost:8501`, adjust the sliders, and click **Predict**.

## Model

| Detail | Value |
|---|---|
| Algorithm | Logistic Regression |
| Features | `radius_mean`, `texture_mean`, `smoothness_mean` |
| Preprocessing | StandardScaler |
| Split | 80/20, stratified, `random_state=42` |
| Labels | Malignant = 1, Benign = 0 |

To retrain: edit `model_training.ipynb`, run all cells to regenerate the `.pkl` files, then update `app.py` if features change.

## Dataset

[Wisconsin Breast Cancer Diagnostic Dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) — 569 samples, 30 features computed from digitized FNA images.

## License

[MIT](LICENSE)
