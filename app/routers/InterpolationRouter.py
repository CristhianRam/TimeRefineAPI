from fastapi import APIRouter
import pandas as pd
from app.schemas.TimeSeries import TimeSeriesRequest, TimeSeriesResponse
from app.schemas.Interpolation import InterpolationOptions
import app.services.InterpolationServices as InterpolationServices

router = APIRouter(
    prefix="/interpolation",
    tags=["Interpolation"])

@router.post("/interpolate", response_model=TimeSeriesResponse,
    summary="Interpolate missing values in time series data")
async def interpolate_time_series(
    request: TimeSeriesRequest,
    options: InterpolationOptions
) -> TimeSeriesResponse:
    """
    Endpoint to interpolate missing values in time series data based on provided interpolation options.

    Args:
        request (TimeSeriesRequest): The input time series data.
        options (InterpolationOptions): Configuration for interpolation.

    Returns:
        TimeSeriesResponse: The time series data with interpolated values.
    """
    df = pd.DataFrame(
        request.values, 
        index=request.timestamps, 
        columns=request.columns)

    interpolated_df = InterpolationServices.interpolate_time_series(df, options)

    return TimeSeriesResponse(
        timestamps=interpolated_df.index.astype(float).tolist(),
        columns=interpolated_df.columns.tolist(),
        values=interpolated_df.values.tolist())