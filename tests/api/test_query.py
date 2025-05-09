from fastapi.testclient import TestClient
from src.main import app
from src.retriever import retriever

client = TestClient(app)

def test_query_endpoint():
    retriever.load_data()
    response = client.post("/similar_responses", json={"question": "What is a hypothesis?"})
    assert response.status_code == 200
    assert "answers" in response.json()
    assert isinstance(response.json()["answers"], list)