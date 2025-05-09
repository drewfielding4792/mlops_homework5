from fastapi import APIRouter
from src.retriever import retriever
from src.models.query import RAGRequest, RAGResponse  # Import the request/response models

router = APIRouter()

@router.post("/similar_responses", response_model=RAGResponse)
def get_similar_responses(request: RAGRequest):
    # Call retriever to get similar responses based on the provided question
    results = retriever.get_similar_responses(request.question)
    
    # Return the results as a RAGResponse object
    return RAGResponse(answers=results)
