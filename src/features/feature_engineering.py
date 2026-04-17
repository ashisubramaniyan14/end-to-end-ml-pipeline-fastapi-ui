import pandas as pd


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["daily_return"] = df["close"].pct_change()
    df["ma_5"] = df["close"].rolling(5).mean()
    df["ma_10"] = df["close"].rolling(10).mean()
    df["volatility_5"] = df["daily_return"].rolling(5).std()
    df["lag_1"] = df["close"].shift(1)
    df["lag_2"] = df["close"].shift(2)

    return df.dropna().reset_index(drop=True)