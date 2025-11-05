from fastapi import FastAPI, Body, Response
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI(
    title="TedAk AI Email Responder API",
    description="Generate AI-powered email responses using OpenAI API",
    version="1.0"
)

# Allow all origins for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Securely load API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# --- ROUTES ---

@app.get("/", response_class=Response)
def home():
    """
    Simple and attractive landing page for the app
    """
    html_content = """
    <html>
        <head>
            <title>TedAk AI Email Assistant</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #3a7bd5, #3a6073);
                    color: white;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                    text-align: center;
                }
                h1 {
                    font-size: 2.8em;
                    margin-bottom: 0.4em;
                }
                p {
                    font-size: 1.2em;
                    margin-bottom: 1.5em;
                    color: #e0e0e0;
                }
                a {
                    background: #ffffff;
                    color: #3a6073;
                    padding: 12px 24px;
                    border-radius: 8px;
                    text-decoration: none;
                    font-weight: bold;
                    font-size: 1.1em;
                    transition: background 0.3s ease;
                }
                a:hover {
                    background: #f1f1f1;
                }
                .links {
                    margin-top: 2em;
                }
                .links a {
                    color: #2b2a2a;
                    text-decoration: underline;
                    font-size: 1em;
                    margin: 0 10px;
                    opacity: 0.85;
                }
                .links a:hover {
                    opacity: 1;
                }
            </style>
        </head>
        <body>
            <h1>✨ TedAk AI Email Responder</h1>
            <p>Generate professional and polite email responses instantly using OpenAI.</p>
            <a href="/gui">🚀 Launch App</a>
            <div class="links">
                <a href="/docs">API Docs</a> |
                <a href="https://github.com/birdcoreone">GitHub</a>
            </div>
        </body>
    </html>
    """
    return Response(content=html_content, media_type="text/html")


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
        return {"error": str(e)}


# --- GRADIO UI ---

def generate_email_response(email_content, tone="Formal"):
    prompt = f"""You are an AI assistant for a customer support team.
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
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

interface = gr.Interface(
    fn=generate_email_response,
    inputs=[
        gr.Textbox(lines=5, placeholder="Paste the customer's email here..."),
        gr.Radio(["Formal", "Casual", "Friendly"], label="Tone", value="Formal"),
    ],
    outputs=gr.Textbox(
        label="AI-Generated Email Response",
        lines=20,
        max_lines=30,
        placeholder="AI response will appear here..."
    ),
    title="TedAk AI Email Assistant",
    description="Paste a customer's email and let AI craft a professional reply instantly."
)

# Mount Gradio interface at /gui
app = gr.mount_gradio_app(app, interface, path="/gui")
