This is a great description for a project\! I've structured it into a complete and professional **README.md** file using standard Markdown formatting, making it clear, easy to read, and actionable for users.

-----

# 📌 Tourism AI Analytics API (FastAPI + Gemini AI)

This project is a high-performance **FastAPI** backend designed for **tourism and hotel data analysis**. It leverages **Google Gemini AI** for deep insights, data summarization, and structured JSON output. It automatically generates analytical **CSV reports** and insightful **visualization charts**.

## 🚀 Features

### ✅ Hotel & Tourism API Endpoints

The following endpoints allow direct access and analysis of the tourism dataset:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/hotels` | Lists all hotels in the database. |
| `GET` | `/hotels/{hotel_id}` | Fetches details for a single hotel by its ID. |
| `GET` | `/distances` | Lists all tourism spot distance records. |
| `GET` | `/joined` | **The main AI analytics route.** Merges hotel + tourism spot data, processes it with Gemini AI, and generates reports. |

### ✅ AI-Powered Insights (`/joined` Endpoint)

The primary analytics route (`/joined`) executes a powerful sequence of operations:

1.  **Data Cleaning** and **Merging** (SQL + CSV files).
2.  Sends the processed dataset to **Google Gemini 2.5 Flash** for analysis.
3.  Receives a **structured JSON insight** adhering to a strict schema.
4.  Saves raw analytical data as **CSV files**.
5.  Generates and saves **Matplotlib visualization charts**.

| Output File | Description | Type |
| :--- | :--- | :--- |
| `state_expense.csv` | State-wise total tourism expenses summary. | CSV |
| `priority_rating.csv` | Hotels sorted and ranked by their rating. | CSV |
| `state_expense_plot.png` | Bar plot visualization of state-wise expense. | PNG |
| `priority_by_rating_plot.png` | Bar chart showing hotel ratings distribution. | PNG |

-----

## 📂 Project Structure

The project maintains a clean, modular structure:

```
.
├── main.py                     # FastAPI application and endpoint definitions
├── tourism.db                  # SQLite local database (hotels & distances)
├── tourism_spots.csv           # Input CSV data for tourism spots
├── state_expense.csv           # 💾 auto-generated AI report
├── priority_rating.csv         # 💾 auto-generated AI report
├── state_expense_plot.png      # 📊 auto-generated visualization
├── priority_by_rating_plot.png # 📊 auto-generated visualization
└── README.md                   # This documentation file
```

-----

## ⚙️ Installation & Setup

### 1️⃣ Create Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Install Dependencies

Install all required Python packages using pip:

```bash
pip install fastapi uvicorn pandas matplotlib google-genai sqlite-utils
```

### 3️⃣ Start the FastAPI Server

Run the application using Uvicorn with auto-reloading enabled for development:

```bash
uvicorn main:app --reload
```

The server will typically run on `http://localhost:8000`.

### 4️⃣ Visit API Docs

FastAPI automatically generates interactive documentation for easy testing:

  * 📘 **Swagger UI** → `http://localhost:8000/docs`
  * 📙 **ReDoc** → `http://localhost:8000/redoc`

### 🔑 Gemini API Key

Before running the `/joined` endpoint, you must configure your Gemini API key in `main.py`:

```python
client = genai.Client(api_key="YOUR_GEMINI_API_KEY") # <-- Update this line!
```

Get your API key from the Google AI Studio:
[https://aistudio.google.com](https://aistudio.google.com)

-----

## 🎯 Using the `/joined` Endpoint

This is the central analytics route. Executing this endpoint will trigger the data pipeline, AI analysis, and local file generation.

**Request:**

```
GET http://localhost:8000/joined
```

**Example AI-Generated JSON Response:**

```json
{
    "state_wise_expense": [
        {
            "state": "Kerala",
            "total_expense": 4200
        },
        // ... more states
    ],
    "priority_by_rating": [
        {
            "name": "Hotel Grand",
            "city": "Kochi",
            "state": "Kerala",
            "rating": 4.8
        },
        // ... more hotels
    ]
}
```

Upon successful execution, the following files will be generated and saved in your project root:

  * `state_expense.csv`
  * `priority_rating.csv`
  * `state_expense_plot.png`
  * `priority_by_rating_plot.png`

-----

## 🧠 How Gemini AI is Used

The project uses the **Google Gemini 2.5 Flash** model for fast, intelligent summarization and structuring.

1.  The Pandas DataFrame is converted into a text representation (e.g., CSV or JSON string).
2.  This string is sent to Gemini with a **highly specific, structured prompt** instructing the model to:
      * Summarize the total tourism expense by state.
      * Sort and list the hotels by their rating.
      * **Crucially**, return the output *only* in a specific, valid JSON format defined by the application.

FastAPI parses the returned JSON for the API response and uses the data to save the local CSV files and Matplotlib plots.

-----

## 🛠 Modifying the Project

The modular structure of FastAPI and the use of Google's robust SDK make this project highly extensible. Potential enhancements include:

  * **Add more AI metrics:** Extend the prompt to analyze customer sentiment, suggest dynamic pricing, or identify high-growth cities.
  * **Add database write endpoints:** Implement `POST`, `PUT`, or `DELETE` endpoints for managing hotel or tourism spot data.
  * **Add Authentication:** Secure the API using JWT or OAuth (e.g., with FastAPI's security features).
  * **Deployment:** Deploy the application on cloud platforms like **AWS**, **Render**, or **Railway**.
  * **Create Dashboards:** Build a rich frontend interface using frameworks like **Next.js** or **React** to visualize the API data.

-----

## 📜 License

This project is open-source for **personal and educational use**.