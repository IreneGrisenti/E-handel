import numpy as np
import pandas as pd

# Total revenue
def total_revenue(df: pd.DataFrame) -> float:
    return round(df["revenue"].sum(), 2)

# Total units
def total_units(df: pd.DataFrame) -> int:
    return df["units"].sum()

# Average order - AOV?

# Revenue per category - What sells?
# Top 3 categories

# Revenue per city - Where?
# Top 3 cities

# Revenue per time - When?