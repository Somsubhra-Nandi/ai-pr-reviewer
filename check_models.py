import os
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Load the specific key we set earlier
load_dotenv(override=True)
api_key = os.getenv("MY_NEW_GEMINI_KEY")

if not api_key:
    print("❌ Error: MY_NEW_GEMINI_KEY not found in .env")
else:
    print(f"🔑 Using Key: ...{api_key[-5:]}")
    genai.configure(api_key=api_key)

    print("\n📡 Connecting to Google to fetch available models...")
    
    try:
        # 2. Ask Google what models exist
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ FOUND: {m.name}")
                available_models.append(m.name)
        
        if not available_models:
            print("\n❌ NO MODELS FOUND. Your API Key might be valid but has no access to Generative AI.")
            print("👉 Solution: Enable 'Generative Language API' in Google Cloud Console.")
            
    except Exception as e:
        print(f"\n💥 CRASH: {e}")