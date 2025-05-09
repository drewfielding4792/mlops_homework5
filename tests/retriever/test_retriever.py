import pytest
from src.retriever import retriever

# This fixture runs once per test session and ensures retriever data is loaded
@pytest.fixture(scope="session", autouse=True)
def preload_retriever():
    retriever.load_data()

def test_get_similar_responses_returns_results():
    question = "What is the capital of France?"
    results = retriever.get_similar_responses(question, top_k=3)
    
    assert isinstance(results, list)
    assert len(results) == 3
    assert all(isinstance(r, str) for r in results)