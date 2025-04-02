import openai
import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI
app = FastAPI()

# Define request model
class RapRequest(BaseModel):
    message: str

# Define API endpoint
@app.post("/rap")
def generate_rap(request: RapRequest):
    prompt = f"Rap battle insult: {request.message}\nAI:"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a funny, savage rap battle opponent. Respond with short, rhyming insults."},
                  {"role": "user", "content": prompt}]
    )

    return {"response": response["choices"][0]["message"]["content"]}
