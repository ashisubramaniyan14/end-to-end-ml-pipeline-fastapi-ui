from pathlib import Path
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from src.features.feature_engineering import add_features


PROCESSED_FILE = Path("data/processed/nvda_processed.csv")
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(parents=True, exist_ok=True)


def train_model() -> Path:
    if not PROCESSED_FILE.exists():
        raise FileNotFoundError(f"Processed file not found: {PROCESSED_FILE}")

    df = pd.read_csv(PROCESSED_FILE)
    df = add_features(df)

    feature_cols = ["daily_return", "ma_5", "ma_10", "volatility_5", "lag_1", "lag_2"]
    X = df[feature_cols]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print(f"Validation Accuracy: {acc:.4f}")
    print(classification_report(y_test, preds))

    model_path = MODEL_DIR / "stock_model.pkl"
    joblib.dump(model, model_path)

    print(f"Saved model to {model_path}")
    return model_path


if __name__ == "__main__":
    train_model()