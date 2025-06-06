from fastapi import FastAPI

from fastapi.responses import RedirectResponse
from src.api import query
from src.retriever import retriever

app = FastAPI(
    title="ML API",
    description="API for ML Model Inference",
    version="1.0.0",
)

@app.on_event("startup")
def preload_data():
    retriever.load_data()

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")
    
app.include_router(query.router)
