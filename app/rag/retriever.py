# Document retrieval logic (embeddings, search)
from app.rag.embed import embed_text
from app.rag.store import VECTOR_STORE


def retrieve_relevant_docs(query: str, top_k: int = 1):
    query_embedding = embed_text(query)

    scored = []
    for doc in VECTOR_STORE:
        score = len(query_embedding.intersection(doc["embedding"]))
        scored.append((score, doc))

    scored.sort(key=lambda x: x[0], reverse=True)

    return [doc for score, doc in scored[:top_k] if score > 0]
