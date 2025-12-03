from pydantic import BaseModel, Field
from app.schemas import TimeSeries
from enum import Enum

class FillMethod(str, Enum):
    mean = "mean"
    median = "median"
    forward_fill = "ffill"
    backward_fill = "bfill"

class OutlierMethod(str, Enum):
    zscore = "zscore"

class CleaningOptions(BaseModel):
    drop_duplicates: bool = Field(
        default=True,
        description="Whether to drop duplicate rows based on timestamps.")

    drop_rows_with_any_nulls: bool = False
    drop_rows_with_all_nulls: bool = False
    drop_rows_with_any_null_in_columns: list[str] = []
    drop_empty_columns: bool = False

    fill_method: FillMethod | None = None

    remove_outliers: bool = False
    outlier_method: str | None = OutlierMethod.zscore