import numpy as np
from app.schemas.Interpolation import InterpolationOptions
import pandas as pd

def interpolate_time_series(
    data: pd.DataFrame,
    options: InterpolationOptions
) -> pd.DataFrame:
    """
    Interpolates missing values in the time series data based on the provided interpolation options.

    Args:
        data (pd.DataFrame): The input time series data with potential missing values.
        options (InterpolationOptions): Configuration for interpolation.

    Returns:
        pd.DataFrame: The time series data with interpolated values.
    """
    if options.method == "linear":
        return data.interpolate(method='linear')
    elif options.method == "nearest":
        return data.interpolate(method='nearest')
    elif options.method == "spline":
        if options.order is None:
            raise ValueError("Order must be specified for spline interpolation.")
        return data.interpolate(method='spline', order=options.order)
    else:
        raise ValueError(f"Unsupported interpolation method: {options.method}")