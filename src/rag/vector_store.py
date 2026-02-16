import os
from pinecone import Pinecone, ServerlessSpec
from src.rag.embeddings import get_embedding
from dotenv import load_dotenv

load_dotenv()

class Memory:
    def __init__(self):
        self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.index_name = "pr-bot-memory"
        self.index = self.pc.Index(self.index_name)

    def store_feedback(self, feedback_text: str, category: str):
        """
        Stores a 'lesson' in the vector database.
        """
        vector = get_embedding(feedback_text)
        
        # We use the text itself as ID (hashed) or just a random one. 
        # Metadata helps us filter later.
        import uuid
        record_id = str(uuid.uuid4())
        
        self.index.upsert(
            vectors=[
                {
                    "id": record_id,
                    "values": vector,
                    "metadata": {
                        "text": feedback_text,
                        "category": category
                    }
                }
            ]
        )
        print(f" Stored memory: {feedback_text[:30]}...")

    def retrieve_memories(self, query_code: str, top_k=3):
        """
        Finds past feedback relevant to the current code.
        """
        vector = get_embedding(query_code)
        
        results = self.index.query(
            vector=vector,
            top_k=top_k,
            include_metadata=True
        )
        
        memories = [match['metadata']['text'] for match in results['matches']]
        return memories