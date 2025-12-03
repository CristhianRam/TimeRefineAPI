from fastapi import APIRouter
import pandas as pd
from app.schemas.TimeSeries import TimeSeriesRequest, TimeSeriesResponse
from app.schemas.Windowing import WindowingOptions, FeatureExtractionOptions, FeaturesResponse
import app.services.WindowingServices as WindowingServices

router = APIRouter(
    prefix="/windowing",
    tags=["Windowing"])

@router.post("/windows", response_model=list[TimeSeriesResponse],
summary="Window time series data")
async def windows(
    request: TimeSeriesRequest,
    windowing_options: WindowingOptions,
) -> list[TimeSeriesResponse]:
    """
    Endpoint to window time series data.

    Args:
        request (TimeSeriesRequest): The input time series data.
        windowing_options (WindowingOptions): Configuration for windowing.

    Returns:
        list[DataFrame]: A list of DataFrames, each containing extracted features from a window.
    """

    df = pd.DataFrame(
        request.values, 
        index=request.timestamps, 
        columns=request.columns)

    windows = WindowingServices.make_windows(df, windowing_options)

    responses = []
    for window in windows:
        responses.append(
            TimeSeriesResponse(
                timestamps=window.index.astype(float).tolist(),
                columns=window.columns.tolist(),
                values=window.values.tolist()
            )
        )

    return responses

@router.post("/feature_extraction", response_model=FeaturesResponse,
    summary="Extract features from time series data")
async def extract_features(
    request: TimeSeriesRequest,
    windowing_options: WindowingOptions,
    feature_extraction_options: FeatureExtractionOptions
) -> FeaturesResponse:
    """
    Endpoint to extract features from time series data windows.

    Args:
        request (TimeSeriesRequest): The input time series data.
        windowing_options (WindowingOptions): Configuration for windowing.
        feature_extraction_options (FeatureExtractionOptions): Configuration for feature extraction.

    Returns:
        FeaturesResponse: The time series data with extracted features.
    """
    df = pd.DataFrame(
        request.values, 
        index=request.timestamps, 
        columns=request.columns)

    features_df = WindowingServices.extract_features(
        df, windowing_options=windowing_options, 
        options=feature_extraction_options)

    return FeaturesResponse(
        columns=features_df.columns.tolist(),
        values=features_df.values.tolist())

    