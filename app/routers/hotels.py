from fastapi import APIRouter
from ..database import get_db

router = APIRouter(prefix="/hotels", tags=["Hotels"])

@router.get("/")
def list_hotels():
    with get_db() as db:
        rows = db.execute("SELECT * FROM hotels").fetchall()
    return [dict(r) for r in rows]

@router.get("/{hotel_id}")
def get_hotel(hotel_id: int):
    with get_db() as db:
        row = db.execute("SELECT * FROM hotels WHERE hotel_id=?", (hotel_id,)).fetchone()
    return dict(row) if row else {"error": "Not found"}
