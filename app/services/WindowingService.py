import numpy as np
import pandas as pd
from app.models.windowing import WindowingOptions

def make_windows(
    data: pd.DataFrame,
    options: WindowingOptions
) -> list[pd.DataFrame]:
    """
    Splits the time series data into overlapping windows.

    Args:
        data (pd.DataFrame): The input time series data.
        options (WindowingOptions): Configuration for windowing.

    Returns:
        list[pd.DataFrame]: A list of DataFrames, each representing a window.
    """
    windows = []
    step_size = options.window_size - options.overlap_size
    for start in range(0, len(data) - options.window_size + 1, step_size):
        end = start + options.window_size
        window = data.iloc[start:end]
        windows.append(window)
    return windows

def extract_features_from_window(
    window: pd.DataFrame,
    options: FeatureExtractionOptions
) -> dict:
    """
    Extracts statistical features from a single window of data.

    Args:
        window (pd.DataFrame): The input window of time series data.
        options (FeatureExtractionOptions): Configuration for feature extraction.

    Returns:
        dict: A dictionary of extracted features.
    """
    features = {}
    for column in window.columns:
        col_data = window[column]
        if options.mean:
            features[f"{column}_mean"] = col_data.mean()
        if options.std:
            features[f"{column}_std"] = col_data.std()
        if options.min:
            features[f"{column}_min"] = col_data.min()
        if options.max:
            features[f"{column}_max"] = col_data.max()
        if options.median:
            features[f"{column}_median"] = col_data.median()
        if options.energy:
            features[f"{column}_energy"] = np.sum(col_data**2)
        if options.entropy:
            prob_dist = col_data.value_counts(normalize=True)
            features[f"{column}_entropy"] = -np.sum(prob_dist * np.log2(prob_dist + 1e-9))
    return features

def extract_features(
    data: pd.DataFrame, 
    windowing_options : WindowingOptions,
    options: FeatureExtractionOptions
    ) -> pd.DataFrame:
    """
    Extracts statistical features from each window of data.

    Args:
        data (pd.DataFrame): The input time series data.
        options: Configuration for feature extraction.

    Returns:
        pd.DataFrame: A DataFrame where each row corresponds to features extracted from a window.
    """
    windows = make_windows(data, windowing_options)
    feature_rows = []
    for window in windows:
        features = extract_features_from_window(window, options)
        feature_rows.append(features)

    return pd.DataFrame(feature_rows)