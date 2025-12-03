from pydantic import BaseModel, Field
from typing import List, Optional

class TimeSeriesRequest(BaseModel):
    timestamps: List[float] = Field(
        ..., description="List of timestamps in seconds or any numeric format."
    )

    # matrix: rows = time, columns = features/sensors
    values: List[List[Optional[float]]] = Field(
        ..., 
        description="2D array where each inner list represents a row of the time series."
    )

    columns: List[str] = Field(
        ..., 
        description="Column names corresponding to each value column."
    )

class TimeSeriesResponse(BaseModel):
    timestamps: List[float]
    columns: List[str]
    values: List[List[float]]