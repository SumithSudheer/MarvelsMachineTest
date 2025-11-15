import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# Absolute paths
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"
STATIC_DIR = BASE_DIR / "app" / "static"

# Ensure folders exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
STATIC_DIR.mkdir(parents=True, exist_ok=True)

def save_outputs(resp: dict):
    """Save CSV and charts to disk safely."""

    if "state_wise_expense" not in resp or "priority_by_rating" not in resp:
        logger.error("Invalid AI response structure. Cannot save output.")
        return

    # Convert to DataFrames
    expense_df = pd.DataFrame(resp["state_wise_expense"])
    rating_df = pd.DataFrame(resp["priority_by_rating"])

    try:
        # Save CSVs
        expense_path = OUTPUT_DIR / "state_expense.csv"
        rating_path = OUTPUT_DIR / "priority_rating.csv"

        expense_df.to_csv(expense_path, index=False)
        rating_df.to_csv(rating_path, index=False)

        # Log file paths
        logger.info(f"Saved: {expense_path}")
        logger.info(f"Saved: {rating_path}")

        # Save charts
        plt.figure(figsize=(8, 5))
        plt.bar(expense_df["state"], expense_df["total_expense"])
        plt.title("State-wise Expense")
        plt.xticks(rotation=45)
        plt.tight_layout()
        chart1 = STATIC_DIR / "state_expense_plot.png"
        plt.savefig(chart1)
        plt.close()

        plt.figure(figsize=(10, 6))
        plt.barh(rating_df["name"], rating_df["rating"])
        plt.title("Priority by Rating")
        plt.tight_layout()
        chart2 = STATIC_DIR / "priority_by_rating_plot.png"
        plt.savefig(chart2)
        plt.close()

        logger.info(f"Saved: {chart1}")
        logger.info(f"Saved: {chart2}")

    except Exception as e:
        logger.error(f"Failed to save output files: {e}")
