from sentence_transformers import SentenceTransformer

# Load the model
model = SentenceTransformer("all-mpnet-base-v2")
print("Model loaded!")

def get_embedding(text: str) -> list[float]:
    """
    Generates a 768-dimensional vector locally.
    No API keys, no limits.
    """
    # Pinecone expects a list, not a numpy array
    return model.encode(text).tolist()