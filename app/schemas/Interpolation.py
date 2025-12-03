from pydantic import BaseModel

class InterpolationMethod(str, Enum):
    linear = "linear"
    nearest = "nearest"
    spline = "spline"

class InterpolationOptions(BaseModel):
    method: InterpolationMethod = Field(
        default=InterpolationMethod.linear, 
        description="Interpolation method to use.")

    order: int | None = Field(
        default = None,
        description = "Order used for spline.")# Only used if method is 'spline'