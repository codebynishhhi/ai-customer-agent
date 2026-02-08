from app.rag.documents import DOCUMENTS
from app.rag.embed import embed_text

VECTOR_STORE = []


def build_store():
    VECTOR_STORE.clear()
    for doc in DOCUMENTS:
        VECTOR_STORE.append({
            "id": doc["id"],
            "text": doc["text"],
            "embedding": embed_text(doc["text"])
        })
