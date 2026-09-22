import pandas as pd
import numpy as np


def validate_prices(df):

    # 1. Check that the index is a DatetimeIndex
    if not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("Index must be a DatetimeIndex")

    # 2. Check that dates are in chronological order
    if not df.index.is_monotonic_increasing:
        raise ValueError("Dates are not in chronological order")

    # 3. Check for duplicate dates
    if df.index.duplicated().any():
        raise ValueError("Duplicate dates found")

    # 4. Check for missing values
    if df.isna().any().any():
        raise ValueError("Missing price values found")

    # 5. Check that every column is numeric
    if not all(pd.api.types.is_numeric_dtype(dtype)
               for dtype in df.dtypes):
        raise ValueError("Non-numeric price data found")

    # 6. Check for infinite values
    if not np.isfinite(df.to_numpy()).all():
        raise ValueError("Infinite values found")

    # 7. Check that all prices are positive
    if (df <= 0).any().any():
        raise ValueError("Non-positive prices found")

    return True