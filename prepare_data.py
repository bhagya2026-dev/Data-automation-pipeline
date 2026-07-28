from pathlib import Path

import pandas as pd


INPUT_FILE = Path("data/raw/customers.csv")
OUTPUT_FILE = Path("data/processed/customers_clean.csv")


def prepare_data():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input file was not found: {INPUT_FILE}"
        )

    df = pd.read_csv(INPUT_FILE)

    # Standardise column names before checking the schema
    df.columns = df.columns.str.strip()

    required_columns = {
        "customer_id",
        "age",
        "monthly_spend",
        "churn"
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    print("Original number of rows:", len(df))

    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["monthly_spend"] = pd.to_numeric(
        df["monthly_spend"],
        errors="coerce"
    )
    df["churn"] = pd.to_numeric(df["churn"], errors="coerce")

    df = df.drop_duplicates()

    invalid_age = ~df["age"].between(18, 100)
    df.loc[invalid_age, "age"] = pd.NA

    invalid_spending = df["monthly_spend"] < 0
    df.loc[invalid_spending, "monthly_spend"] = pd.NA

    invalid_churn = ~df["churn"].isin([0, 1])
    df.loc[invalid_churn, "churn"] = pd.NA

    print("\nMissing or invalid values:")
    print(df.isna().sum())

    df = df.dropna(
        subset=["customer_id", "age", "monthly_spend", "churn"]
    )

    df["spending_band"] = pd.cut(
        df["monthly_spend"],
        bins=[0, 4000, 6000, float("inf")],
        labels=["Low", "Medium", "High"]
    )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print("\nClean number of rows:", len(df))
    print("\nCleaned data:")
    print(df)

    return df


if __name__ == "__main__":
    prepare_data()