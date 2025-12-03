from fastapi import FastAPI
# Routers
from app.routers.CleaningRouter import router as cleaning_router


app = FastAPI(
    title="TimeRefine API",
    description="API for time series data preprocessing and feature extraction.",
    version="0.1.0"
)

app.include_router(cleaning_router)

@app.get("/")
def root():
    return {"message": "TimeRefine API running!"}

@app.get("/health")
def health():
    return {"status": "ok"}