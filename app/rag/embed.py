def embed_text(text: str) -> set:
    """
    Simple bag-of-words embedding (learning version)
    """
    return set(text.lower().split())
