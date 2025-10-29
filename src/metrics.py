import numpy as np
import pandas as pd

# Total revenue
def total_revenue(df: pd.DataFrame) -> float:
    return round(df["revenue"].sum(), 2)

# Total units
def total_units(df: pd.DataFrame) -> int:
    return df["units"].sum()

# Average order - AOV?
def average_order(df: pd.DataFrame) -> float:
    return round(total_revenue(df) / df["order_id"].nunique(), 2)

# Revenue per category - What sells?
def revenue_per_category(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("category", observed=True)
        .agg(tot_rev_cat=("revenue", "sum"))
        .sort_values("tot_rev_cat", ascending=False)
        .reset_index())

# Revenue per city - Where?
def revenue_per_city(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("city", observed=True)
        .agg(tot_rev_city=("revenue", "sum"))
        .sort_values("tot_rev_city", ascending=False)
        .reset_index())

# Revenue per time - When?
def revenue_per_month(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()
    df["month"] = df["date"].dt.to_period("M").astype(str)

    return (
        df.groupby("month", observed=True)
        .agg(rev_per_month=("revenue", "sum"))
        .sort_values("month")
        .reset_index())