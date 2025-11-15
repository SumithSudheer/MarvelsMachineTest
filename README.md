
This project is a complete, Python-based system that integrates tourism data from SQLite and CSV sources, processes it using Google Gemini AI for analytical insights, and exposes its functionality via a high-performance FastAPI backend.

This architecture demonstrates proficiency in data engineering, multi-source data integration, AI processing, visualization, and API development, making it ideal for machine test evaluations.

## 🚀 Features Overview

### ✅ 1. Multi-Source Data Integration & Cleaning
The system efficiently handles data from different sources and prepares it for AI analysis:
- **Reads Data**: Fetches hotel and distance records from SQLite (`data/tourism.db`).
- **Imports Data**: Loads detailed tourism spot information from CSV (`data/tourism_spots.csv`).
- **Merges Data**: Combines both datasets using common keys (City + State).
- **Data Cleaning**: Standardizes column names, removes duplicates, handles missing values, and normalizes location names for consistent merging.

### ✅ 2. AI-Powered Data Analysis (Gemini 2.5 Flash)
The cleaned dataset is sent to the Gemini AI model, which is instructed to return strict JSON containing critical business insights:

| Insight              | Description                                      | Example JSON Structure                  |
|----------------------|--------------------------------------------------|-----------------------------------------|
| A. State-wise Expense | Total tourism expenses aggregated by state.     | `{"state": "Kerala", "total_expense": 5400}` |
| B. Priority Ranking   | Tourism spots/hotels sorted by the highest rating. | `{"name": "Taj Hotel", "city": "Mumbai", "rating": 4.9}` |

### ✅ 3. Output Generation
AI results are persisted to the filesystem for reporting and archival purposes:

| Type          | Path                          | Description                          |
|---------------|-------------------------------|--------------------------------------|
| 📄 CSV Files | `outputs/state_expense.csv`  | Detailed state-wise expenditure report. |
| 📄 CSV Files | `outputs/priority_rating.csv`| Ranked list of hotels by rating.     |
| 📊 Visual Charts | `app/static/state_expense_plot.png` | Bar chart visualization of state expenditure. |
| 📊 Visual Charts | `app/static/priority_by_rating_plot.png` | Visualization of priority rankings. |

### ✅ 4. REST API Endpoints (FastAPI)
The application provides a robust API layer for accessing and triggering analytics:

| Method | Endpoint              | Description                                      |
|--------|-----------------------|--------------------------------------------------|
| GET    | `/`                   | API health check.                                |
| GET    | `/hotels`             | List all hotels.                                 |
| GET    | `/hotels/{id}`        | Get specific hotel by ID.                        |
| GET    | `/distances`          | List all stored distances.                       |
| GET    | `/analytics/process`  | Primary route: Triggers the Merge → Clean → AI Summary → Save Outputs pipeline. |

## 📂 Project Structure
The project follows a modular, scalable architecture:

```
tourism-ai-project/
│
├── app/
│   ├── main.py             # FastAPI entry point, application setup
│   ├── config.py           # Loads settings from config.json
│   ├── database.py         # SQLite connection and query handlers
│   ├── ai_service.py       # Handles data formatting and Gemini API calls
│   ├── utils.py            # Data cleaning and plotting utilities
│   ├── routers/            # Modular endpoint definitions
│   │   ├── hotels.py
│   │   ├── distances.py
│   │   └── analytics.py    # The core processing endpoint
│   └── static/             # Stores generated visualization PNGs
│
├── data/                   # Input data sources
│   ├── tourism.db          # SQLite DB (must be initialized first)
│   └── tourism_spots.csv
│
├── outputs/                # Generated CSV analytical reports
│
├── config.json             # Global configuration settings
├── requirements.txt        # Project dependencies
└── README.md
```

## 🛠️ Installation & Setup

### 1. Clone the Project and Create Directories
```bash
git clone <repo-url>
cd tourism-ai-project

```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
Ensure you have the following installed (typically via a `requirements.txt`):
```bash
pip install -r requirements.txt
```

### 4. Configure API Key and Database
- **Configure API Key**: Update the `config.json` file with your Google Gemini API key:
  ```json
  {
    "db_path": "data/tourism.db",
    "csv_path": "data/tourism_spots.csv",
    "gemini_api_key": "YOUR_GEMINI_KEY_HERE"
  }
  ```
- **Initialize Database**: You must run a separate script (e.g., `initialize_db.py`) once to populate `data/tourism.db` with the initial hotel and distance data before running the API.

## ▶️ Running the API
Start the FastAPI server using Uvicorn:
```bash
uvicorn app.main:app --reload
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Interactive API Docs
Explore and test all endpoints directly using the auto-generated documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## ▶️ Running the Dashboard
Start the Streamlit Dashboard:
```bash
streamlit run app/dashboard.py
```

The Dashboard will be available at: [http://localhost:8501](http://localhost:8501)

## 📊 Outputs Generated
The CSV files and PNG charts will be generated/overwritten every time the `/analytics/process` endpoint is called.

### CSV Reports
| File                  | Location    |
|-----------------------|-------------|
| `state_expense.csv`   | `/outputs/` |
| `priority_rating.csv` | `/outputs/` |

### Visualization Charts
| File                              | Location      |
|-----------------------------------|---------------|
| `state_expense_plot.png`          | `/app/static/` |
| `priority_by_rating_plot.png`     | `/app/static/` |

## 💡 Design Principles Used
- **Modular Architecture**: Clear separation of concerns (Routers, Services, Utils, Database).
- **Configuration-First**: All sensitive settings are managed via `config.json`.
- **Data Best Practices**: Leverages Pandas for efficient data manipulation.
- **AI Validation**: Uses prompt engineering and JSON schema enforcement to ensure structured, predictable output from the LLM.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author
**Sumith Sudheer**  
Backend + AI Developer  
FastAPI • Django • ML • AWS  

- [LinkedIn](https://linkedin.com/in/sumith-sudheer) <!-- Optional: Add actual links -->
- [GitHub](https://github.com/sumith-sudheer)
- Email: sumith@example.com <!-- Optional: Add actual email -->

---