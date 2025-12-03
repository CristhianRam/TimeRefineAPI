import pandas as pd
import numpy as np
from app.schemas.Cleaning import CleaningOptions

def clean_time_series(
    data: pd.DataFrame,
    options: CleaningOptions
) -> pd.DataFrame:
    """
    Cleans the time series data based on the provided cleaning options.

    Args:
        data (pd.DataFrame): The input time series data.
        options (CleaningOptions): Configuration for cleaning.

    Returns:
        pd.DataFrame: The cleaned time series data.
    """
    if options.drop_duplicates:
        data = data.drop_duplicates()

    if options.drop_rows_with_any_nulls:
        data = data.dropna(how='any')

    if options.drop_rows_with_all_nulls:
        data = data.dropna(how='all')

    if options.drop_rows_with_any_null_in_columns:
        data = data.dropna(subset=options.drop_rows_with_any_null_in_columns, how='any')

    if options.drop_empty_columns:
        data = data.dropna(axis=1, how='all')

    if options.fill_method:
        if options.fill_method == "mean":
            data = data.fillna(data.mean())
        elif options.fill_method == "median":
            data = data.fillna(data.median())
        elif options.fill_method == "ffill":
            data = data.fillna(method='ffill')
        elif options.fill_method == "bfill":
            data = data.fillna(method='bfill')

    if options.remove_outliers:
        if options.outlier_method == "zscore":
            from scipy import stats
            z_scores = np.abs(stats.zscore(data.select_dtypes(include=[np.number]), nan_policy='omit'))
            filtered_entries = (z_scores < 3).all(axis=1)
            data = data[filtered_entries]

    return data