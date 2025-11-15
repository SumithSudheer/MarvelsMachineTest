import json
import logging
import sqlite3

import pandas as pd
import matplotlib.pyplot as plt
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai


# -----------------------------------------
# Logging Setup
# -----------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# -----------------------------------------
# FastAPI App
# -----------------------------------------
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def home():
    return {"message": "FastAPI Boilerplate Running!"}


# -----------------------------------------
# Database Helpers
# -----------------------------------------
DB_PATH = "tourism.db"   # Your SQLite database file


def get_db_connection():
    """Return SQLite connection with dict rows."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# -----------------------------------------
# Basic Endpoints
# -----------------------------------------
@app.get("/hotels")
def get_hotels():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM hotels").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/hotels/{hotel_id}")
def get_hotel(hotel_id: int):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT * FROM hotels WHERE hotel_id = ?", (hotel_id,)
    ).fetchone()
    conn.close()
    return dict(row) if row else {"error": "Hotel not found"}


@app.get("/distances")
def get_distances():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM distances").fetchall()
    conn.close()
    return [dict(row) for row in rows]


# -----------------------------------------
# GEMINI CLIENT
# -----------------------------------------
client = genai.Client(
    api_key="AIzaSyB_yTYidk0EkSjqeCqn_zqtNy11CJ_8g8Q"
)


# -----------------------------------------
# AI Summary Function
# -----------------------------------------
def get_summary_gen_ai(df: pd.DataFrame):
    df_text = df.to_string()

    prompt = f"""
    You are a data analyst. Analyze the following dataset:

    {df_text}

    Return ONLY valid JSON. Do not include explanations or text outside JSON.

    The JSON must follow this exact structure:

    {{
        "state_wise_expense": [
            {{
                "state": "",
                "total_expense": 0
            }}
        ],
        "priority_by_rating": [
            {{
                "name": "",
                "city": "",
                "state": "",
                "rating": 0
            }}
        ]
    }}

    Rules:
    - Calculate state_wise_expense by summing expense or price_per_night.
    - Sort priority_by_rating from highest rating to lowest.
    - No content outside JSON.
    """

    prompt = json.dumps(prompt, indent=2)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text
    logger.info(text)

    # Clean possible markdown wrappers
    if text.startswith("```"):
        text = text.strip().replace("```json", "").replace("```", "").strip()

    return json.loads(text)


# -----------------------------------------
# CSV & Visualization Generator
# -----------------------------------------
def create_visualisation_and_csv(resp):
    expense_df = pd.DataFrame(resp["state_wise_expense"])
    rating_df = pd.DataFrame(resp["priority_by_rating"])

    # Save CSV files
    expense_df.to_csv("state_expense.csv", index=False)
    rating_df.to_csv("priority_rating.csv", index=False)

    # Charts
    plt.figure(figsize=(8, 5))
    plt.bar(expense_df["state"], expense_df["total_expense"])
    plt.title("State-wise Tourism Expense")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("state_expense_plot.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.barh(rating_df["name"], rating_df["rating"])
    plt.title("Priority by Rating")
    plt.tight_layout()
    plt.savefig("priority_by_rating_plot.png")
    plt.close()


# -----------------------------------------
# Merged Data Endpoint
# -----------------------------------------
@app.get("/joined")
def get_joined_data():
    logger.debug("Joining hotel and tourism data")

    conn = get_db_connection()

    # Load SQL + CSV
    hotel_df = pd.read_sql("SELECT * FROM hotels", conn)
    tourism_df = pd.read_csv("tourism_spots.csv")

    conn.close()

    # -----------------------------
    # Clean Column Names
    # -----------------------------
    hotel_df.columns = hotel_df.columns.str.lower().str.replace(" ", "_")
    tourism_df.columns = tourism_df.columns.str.lower().str.replace(" ", "_")

    # Remove duplicates
    hotel_df = hotel_df.drop_duplicates()
    tourism_df = tourism_df.drop_duplicates()

    # Trim strings
    hotel_df = hotel_df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    tourism_df = tourism_df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    # Fill missing values
    hotel_df = hotel_df.fillna({"rating": 0, "price_per_night": 0})
    tourism_df = tourism_df.fillna({"rating": 0, "entry_fee": 0})

    # Capitalize city/state for merge accuracy
    for col in ["city", "state"]:
        hotel_df[col] = hotel_df[col].str.title()
        tourism_df[col] = tourism_df[col].str.title()

    # -----------------------------
    # MERGE
    # -----------------------------
    merged = pd.merge(
        hotel_df,
        tourism_df,
        on=["city", "state"],
        how="left",
        suffixes=("_hotel", "_spot")
    )

    logger.info("Merged dataset created")

    # -----------------------------
    # AI Summary + Charts
    # -----------------------------
    resp = get_summary_gen_ai(merged)
    create_visualisation_and_csv(resp)

    return resp
