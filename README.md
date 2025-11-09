# AI-Powered Email Responder

## 1. Project Overview
The **AI-Powered Email Responder** is a mini-project developed for the KsTU Artificial Intelligence cohort.  
It leverages OpenAI GPT models to generate professional email responses based on customer emails.  
The system can produce responses in different tones (Formal, Friendly, Casual) and is designed to streamline customer support workflows.

---

🚀 Features

✉️ Generate professional, friendly, or casual email responses

⚡ FastAPI backend for API requests

🧩 Gradio frontend for easy interaction

🔐 Secure API key management using .env

☁️ Ready for deployment on Render

## 2. Project Structure
AI-Powered-Email-Assistant/
├─ app.py # FastAPI backend serving email generation
├─ email_ui.py # Optional Gradio GUI for user-friendly interface
├─ .env # Environment file storing API key securely
├─ requirements.txt # Python dependencies
├─ sample_output.json # Sample JSON requests and responses
└─ README.md # Project documentation


---

## 3. Setup Instructions

### 3.1 Install Python Dependencies
Ensure Python 3.12+ is installed.  
Then, install dependencies:
```bash
pip install -r requirements.txt
```

### 3.2 Clone Repository 
```bash
git clone https://github.com/<your-username>/AI-powered-email-responder.git
cd AI-powered-email-responder
```

###3.3 Create .env File

Create a .env file in the project root:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
This ensures your API key is not hardcoded in main.py


### 3.4 Running the FastAPI Server

Start the server with:

```bash
uvicorn app:app --reload
```

The API will be accessible at: http://127.0.0.1:8000/docs

# 3.5 Optional Gradio GUI

If using email_ui.py:
```bash
python email_ui.py
```

This launches a user-friendly web interface to input customer emails and generate responses.

# 4. API Usage
Endpoint: POST /email/

Request JSON Example:

```json
{
  "email_content": "Hello, I am interested in your digital service packages for small businesses. Could you provide details?",
  "tone": "Formal"
}
```

### API Email Example
![API CustomerEmail](/docs/screenshots/Gui_interface.png)
![API CustomerEmail](/docs/screenshots/customer_input.png)


Response JSON Example:
```json
{
  "response": "Subject: Re: Inquiry About Digital Services\n\nDear [Customer Name],\n\nThank you for your inquiry about our digital service packages for small businesses..."
}
```

### API Email Example
![API Response](/docs/screenshots/Response.png)
![API Response](/docs/screenshots/api_interface.png)



# 5. Security & Notes

API Key Handling: Do not hardcode your OpenAI API key in public repositories.

.exe Build: Using PyInstaller, the project can be packaged into a standalone .exe.

Offline Use: The .exe only works with an active internet connection since it relies on the OpenAI API.

👨🏽‍💻 Author

Teddy Boamah
BTech Artificial Intelligence – KsTU AI Cohort 1
🚀 ALX Certified Data Scientist | Founder of Tedak Group of Companies

🧾 License

This project is licensed under the MIT License — feel free to use, modify, and share responsibly.
