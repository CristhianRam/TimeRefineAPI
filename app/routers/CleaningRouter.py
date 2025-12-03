from fastapi import APIRouter
import pandas as pd
from app.schemas.TimeSeries import TimeSeriesRequest, TimeSeriesResponse
from app.schemas.Cleaning import CleaningOptions
import app.services.CleaningServices as CleaningServices

router = APIRouter(
    prefix="/cleaning",
    tags=["Cleaning"])

@router.post("/clean", response_model=TimeSeriesResponse)
async def clean_time_series(
    request: TimeSeriesRequest,
    options: CleaningOptions
) -> TimeSeriesResponse:
    """
    Endpoint to clean time series data based on provided cleaning options.

    Args:
        request (TimeSeriesRequest): The input time series data.
        options (CleaningOptions): Configuration for cleaning.

    Returns:
        TimeSeriesResponse: The cleaned time series data.
    """
    # generate DataFrame from request
    df = pd.DataFrame(
        request.values, 
        index=request.timestamps, 
        columns=request.columns)

    # clean the data
    cleaned_df = CleaningServices.clean_time_series(df, options)

    return TimeSeriesResponse(
        timestamps=cleaned_df.index.astype(float).tolist(),
        columns=cleaned_df.columns.tolist(),
        values=cleaned_df.values.tolist())

    