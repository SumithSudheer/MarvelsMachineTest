from fastapi import FastAPI
from .routers import hotels, analytics

app = FastAPI(title="AI Tourism Data Engine")

app.include_router(hotels.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"message": "AI Tourism API Running!"}
