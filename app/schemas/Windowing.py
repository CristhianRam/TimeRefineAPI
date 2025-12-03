from pydantic import BaseModel, Field

class WindowingOptions(BaseModel):
    window_size: int = Field(
        default=5,
        description="Size of the moving window.")

    overlap_size: int = Field(
        default=0,
        description="Number of overlapping points between consecutive windows.")

class FeatureExtractionOptions(BaseModel):
    mean: bool = True
    std: bool = True
    min: bool = False
    max: bool = False
    median: bool = False
    energy: bool = False
    entropy: bool = False

class FeaturesResponse(BaseModel):
    columns: list[str] = Field(
        ...,
        description="List of feature names extracted from the time series data.")

    values: list[list[float]] = Field(
        ...,
        description="Extracted features values from the time series data.")