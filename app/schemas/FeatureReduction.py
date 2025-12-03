from pydantic import BaseModel, Field
from enum import Enum

class FeatureReductionMethod(str, Enum):
    pca = "PCA"
    tsne = "t-SNE"
    umap = "UMAP"

class FeatureReductionOptions(BaseModel):
    method: FeatureReductionMethod = Field(
        default=FeatureReductionMethod.pca,
        description="Feature reduction method to use.")

    n_components: int = Field(
        default=2,
        description="Number of components to reduce to.")  # Number of components to reduce to