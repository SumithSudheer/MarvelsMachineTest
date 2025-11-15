This is an excellent, detailed description of a robust project. I'll condense and reformat the content into a standard, professional **README.md** file format, using Markdown for clear structure and visual appeal.

Here is the requested README file content:

```markdown
# 📌 Tourism AI Analytics API (FastAPI + Gemini AI)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![AI-Model](https://img.shields.io/badge/AI%20Engine-Gemini%202.5%20Flash-0B6BEA.svg)](https://ai.google.com/gemini/api)

A complete, Python-based system that integrates multi-source tourism data (SQLite, CSV), processes it using Google **Gemini AI** for deep analytical insights, and exposes its functionality via a high-performance **FastAPI** backend. This project demonstrates proficiency in the full data-to-API pipeline, covering data engineering, AI processing, visualization, and API development.

---

## 🚀 Features

This architecture is built around four core functional pillars:

### 1. Multi-Source Data Integration & Cleaning 🧹
The system efficiently merges and prepares data from disparate sources for reliable AI analysis:

* **Data Sources:** Fetches records from **SQLite** (`data/tourism.db`) and **CSV** (`data/tourism_spots.csv`).
* **Integration:** Combines datasets using common keys (`city` + `state`).
* **Cleaning Logic:** Includes standardization of column names, removal of duplicates, graceful handling of missing values (numeric/text), and normalization of city/state values.

### 2. AI-Powered Data Analysis (Gemini 2.5 Flash) 🧠
The cleaned dataset is sent to the Gemini AI model, which is strictly instructed to return **JSON** containing critical business insights:

| Insight | Description | Example JSON Structure |
| :--- | :--- | :--- |
| **A. State-wise Expense** | Total tourism expenses aggregated by state. | `{"state": "Kerala", "total_expense": 5400}` |
| **B. Priority Ranking** | Tourism spots/hotels sorted by the highest rating. | `{"name": "Taj Hotel", "city": "Mumbai", "rating": 4.9}` |

### 3. Output Generation & Persistence 💾
AI results are converted into structured reports and archival visualizations:

| Type | Path | Description |
| :--- | :--- | :--- |
| **CSV Reports** | `outputs/state_expense.csv` | Detailed state-wise expenditure report. |
| | `outputs/priority_rating.csv` | Ranked list of hotels by rating. |
| **Visual Charts** | `app/static/state_expense_plot.png` | Bar chart visualization of state expenditure. |
| | `app/static/priority_by_rating_plot.png` | Visualization of priority rankings. |

### 4. REST API Endpoints (FastAPI) 🌐
A robust API layer provides access to both the raw data and the analytical pipeline:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | API health check. |
| `GET` | `/hotels` | List all hotels. |
| `GET` | `/distances` | List all stored distances. |
| `GET` | `/analytics/process` | **Primary Route**: Triggers the entire Merge → Clean → AI Summary → Save Outputs pipeline. |

---

## 📂 Project Structure

A modular and scalable architecture ensuring clear separation of concerns:

```

tourism-ai-project/
│
├── app/
│   ├── main.py             \# FastAPI entry point
│   ├── config.py           \# Loads settings
│   ├── database.py         \# SQLite handlers
│   ├── ai\_service.py       \# Data formatting and Gemini API calls (Core Intelligence)
│   ├── utils.py            \# Data cleaning and plotting utilities
│   ├── routers/            \# Modular endpoint definitions (hotels, distances, analytics)
│   └── static/             \# Stores generated visualization PNGs
│
├── data/                   \# Input data sources (tourism.db, tourism\_spots.csv)
├── outputs/                \# Generated CSV analytical reports
├── config.json             \# Global configuration (API Key, paths)
└── requirements.txt        \# Project dependencies

````

---

## 🛠️ Installation & Setup

### 1. Clone the Project

```bash
git clone <repo-url>
cd tourism-ai-project
````

### 2\. Create Virtual Environment and Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3\. Configure API Key

Update the `config.json` file with your **Google Gemini API key**:

```json
{
  "db_path": "data/tourism.db",
  "csv_path": "data/tourism_spots.csv",
  "gemini_api_key": "YOUR_GEMINI_KEY_HERE"
}
```

### 4\. Run the API

Start the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

### 5\. Interactive Docs

Explore and test all endpoints directly via the auto-generated Swagger UI documentation: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

-----

## 📘 How the AI Processing Works

The core intelligence is managed in `app/ai_service.py`:

1.  A Pandas DataFrame (full merged dataset) is converted into a structured string format.
2.  This data, along with a detailed **system prompt**, is sent to the `gemini-2.5-flash` model.
3.  The prompt strictly enforces a **JSON output schema** to ensure the model performs the required aggregation and sorting tasks reliably.
4.  The valid JSON response is parsed back into the API, which then uses the data to generate the final local CSV reports and Matplotlib charts.

-----

## 💡 Design Principles

  * **Modular Architecture:** Clear separation of concerns (Routers, Services, Utils).
  * **Configuration-First:** All sensitive settings are managed via `config.json`.
  * **Single Responsibility Principle:** Functions are small and focused (`clean_data()`, `generate_plot()`).
  * **AI Validation:** Uses strong prompt engineering to enforce structured, predictable JSON output from the LLM.

-----

**Author:** Sumith Sudheer

