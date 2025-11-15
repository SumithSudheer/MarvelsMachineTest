import json
import logging
import pandas as pd
from google import genai
from .config import Config

logger = logging.getLogger(__name__)
config = Config()

client = genai.Client(api_key=config.gemini_key)

def analyze_dataset(df: pd.DataFrame) -> dict:
    """
    Sends the merged tourism dataset to Gemini AI and returns structured JSON.
    """

    prompt = f"""
    You are a tourism data analyst. Analyze this dataset and return structured JSON:

    DATAFRAME:
    {df.to_string()}

    STRICT JSON FORMAT (NO TEXT OUTSIDE JSON):
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
    - Group by state and sum "price_per_night" or "entry_fee".
    - Sort priority_by_rating by rating descending.
    - DO NOT include Markdown.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        logger.error("Gemini returned invalid JSON.")
        return {"error": "AI response invalid"}
