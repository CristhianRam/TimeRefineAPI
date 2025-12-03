from pydantic import BaseModel

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