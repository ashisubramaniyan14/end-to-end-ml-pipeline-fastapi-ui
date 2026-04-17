from pathlib import Path
import pandas as pd
import yfinance as yf


RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)


def fetch_stock_data(symbol: str = "NVDA", period: str = "2y", interval: str = "1d") -> Path:
    df = yf.download(symbol, period=period, interval=interval, auto_adjust=False)

    if df.empty:
        raise ValueError("No data returned from Yahoo Finance.")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()
    df.columns = [str(col).strip().lower().replace(" ", "_") for col in df.columns]

    rename_map = {
        "date": "date",
        "datetime": "date",
        "open": "open",
        "high": "high",
        "low": "low",
        "close": "close",
        "adj_close": "adj_close",
        "adj close": "adj_close",
        "volume": "volume",
    }

    df = df.rename(columns=rename_map)

    output_path = RAW_DIR / f"{symbol.lower()}_raw.csv"
    df.to_csv(output_path, index=False)

    print("Columns in raw file:", list(df.columns))
    print(f"Saved raw data to {output_path}")
    return output_path


if __name__ == "__main__":
    fetch_stock_data()