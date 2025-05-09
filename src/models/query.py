from pydantic import BaseModel
from typing import List

#whatever we define populates in swagger docs.
class RAGRequest(BaseModel):
    question: str

class RAGResponse(BaseModel):
    answers: List[str]
