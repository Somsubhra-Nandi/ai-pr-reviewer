import sys
import os

# Add the project root to python path so we can import src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.rag.vector_store import Memory

def main():
    brain = Memory()
    
    # Let's seed it with some "Senior Dev" wisdom
    lessons = [
        ("Never use print() in production code. Use the logger instead.", "clean_code"),
        ("Always add type hints to function arguments.", "style"),
        ("Avoid hardcoding API keys. Use environment variables.", "security"),
        ("In FastAPI, use Pydantic models for request bodies, not raw dicts.", "framework_specific"),
        ("Use 'async def' only if you are awaiting something inside.", "performance")
    ]
    
    print(" Teaching the bot...")
    for text, category in lessons:
        brain.store_feedback(text, category)
    print(" Done! The bot is now smarter.")

if __name__ == "__main__":
    main()