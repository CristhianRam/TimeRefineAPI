from pydantic import BaseModel

class TimeSeriesRequest(BaseModel):
    timestamps: List[str] = Field(..., description="List of timestamps in ISO format.")

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