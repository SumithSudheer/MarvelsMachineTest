import json
import logging

class Config:
    """Loads project configuration from config.json."""

    def __init__(self, path="config.json"):
        try:
            with open(path, "r") as f:
                self.data = json.load(f)
        except Exception as e:
            logging.error(f"Failed to load config.json: {e}")
            raise

    @property
    def db_path(self):
        return self.data.get("db_path")

    @property
    def csv_path(self):
        return self.data.get("csv_path")

    @property
    def gemini_key(self):
        return self.data.get("gemini_api_key")
