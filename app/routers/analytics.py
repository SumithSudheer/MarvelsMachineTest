import pandas as pd
from fastapi import APIRouter
from ..database import get_db
from ..config import Config
from ..ai_service import analyze_dataset
from ..utils import save_outputs

router = APIRouter(prefix="/analytics", tags=["Analytics"])
config = Config()

@router.get("/process")
def process_data():
    with get_db() as db:
        hotels = pd.read_sql("SELECT * FROM hotels", db)

    tourism = pd.read_csv(config.csv_path)

    hotels.columns = hotels.columns.str.lower().str.replace(" ", "_")
    tourism.columns = tourism.columns.str.lower().str.replace(" ", "_")

    hotels = hotels.drop_duplicates()
    tourism = tourism.drop_duplicates()

    hotels = hotels.fillna({"rating": 0, "price_per_night": 0})
    tourism = tourism.fillna({"rating": 0, "entry_fee": 0})

    merged = pd.merge(
        hotels, tourism, on=["city"], how="left"
    )

    ai_response = analyze_dataset(merged)
    save_outputs(ai_response)

    return ai_response
