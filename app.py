from fastapi import FastAPI, Body
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI
app = FastAPI(
    title="TedAk AI Email Responder API",
    description="Generate AI-powered email responses using OpenAI API",
    version="1.0"
)

# Fetch API key securely
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)
@app.get("/")
def home():
    return {"message": "Welcome to the AI Email Responder API!"}

@app.post("/email/")
def generate_email(
    email_content: str = Body(..., description="Customer email content"),
    tone: str = Body("Formal", description="Tone of the response: Formal, Friendly, or Casual")
):
    """
    Generate a professional email response using the OpenAI API.
    """
    prompt = f"""
    You are an AI assistant for a customer support team.
    Generate a {tone} email response to the following customer message:

    {email_content}

    Make the response polite, clear, and professional.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        ai_message = response.choices[0].message.content.strip()
        return {"response": ai_message}

    except Exception as e:
        return {"error": f"API Error: {str(e)}"}
