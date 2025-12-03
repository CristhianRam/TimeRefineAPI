from fastapi import APIRouter
import pandas as pd
from app.schemas.TimeSeries import TimeSeriesRequest, TimeSeriesResponse
from app.schemas.Windowing import WindowingOptions, FeatureExtractionOptions
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
    # generate DataFrame from request
    df = pd.DataFrame(
        request.values, 
        index=request.timestamps, 
        columns=request.columns)

    # create windows
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