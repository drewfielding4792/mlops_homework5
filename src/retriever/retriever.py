import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from src.models.helpers import clean_text
import pickle
import os

MODEL = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
CSV_PATH = "data/6000_all_categories_questions_with_excerpts.csv"
PICKLE_PATH = "data/embedding_store.pkl"

df = None
embedding_matrix = None

def load_data():
    global df, embedding_matrix
    if os.path.exists(PICKLE_PATH):
        with open(PICKLE_PATH, "rb") as f:
            store = pickle.load(f)
            df = store["df"]
            embedding_matrix = store["embedding_matrix"]
    else:
        df = pd.read_csv(CSV_PATH)
        df = df[df['wikipedia_excerpt'].notna()].copy()
        df['embedding'] = df['wikipedia_excerpt'].apply(lambda x: MODEL.encode(x).tolist())
        embedding_matrix = np.array(df['embedding'].tolist())
        with open(PICKLE_PATH, "wb") as f:
            pickle.dump({"df": df, "embedding_matrix": embedding_matrix}, f)

def get_similar_responses(question: str, top_k=3) -> list:
    if df is None or embedding_matrix is None:
        raise RuntimeError("Retriever data has not been loaded. Call load_data() first.")
    clean_question = clean_text(question)
    query_vec = MODEL.encode(clean_question)
    scores = cosine_similarity([query_vec], embedding_matrix)[0]
    top_indices = scores.argsort()[-top_k:][::-1]
    return df.iloc[top_indices]['wikipedia_excerpt'].tolist()