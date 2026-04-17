from pathlib import Path
import pandas as pd


RAW_FILE = Path("data/raw/nvda_raw.csv")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_processed_dataset() -> Path:
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Raw file not found: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE)
    df.columns = [c.lower() for c in df.columns]

    required = ["date", "open", "high", "low", "close", "volume"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    numeric_cols = ["open", "high", "low", "close", "volume"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna().drop_duplicates().sort_values("date").reset_index(drop=True)
    df["target"] = (df["close"].shift(-1) > df["close"]).astype(int)
    df = df.iloc[:-1]

    output_path = PROCESSED_DIR / "nvda_processed.csv"
    df.to_csv(output_path, index=False)

    print(f"Saved processed dataset to {output_path}")
    return output_path


if __name__ == "__main__":
    build_processed_dataset()