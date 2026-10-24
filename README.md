# AI Resume Email Automation

An AI-powered FastAPI application that automates resume screening and HR email responses.

## Features

- 📄 Upload Resume (PDF)
- 📖 Read Resume Content
- 📧 Extract Candidate Email Automatically
- 🤖 Analyze Resume using Google Gemini AI
- ✉️ Generate Professional HR Email
- 📨 Automatically Send Email via Gmail SMTP

---

## Tech Stack

- Python
- FastAPI
- Google Gemini API
- PyPDF
- SMTP (Gmail)
- Regex
- JSON
- dotenv



### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create .env

```env
API_KEY=YOUR_GEMINI_API_KEY
SENDER_EMAIL=YOUR_GMAIL
APP_PASSWORD=YOUR_GOOGLE_APP_PASSWORD
```

### Run

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Workflow

```text
Upload Resume
      │
      ▼
Read PDF
      │
      ▼
Extract Candidate Email
      │
      ▼
Gemini AI Resume Analysis
      │
      ▼
Generate HR Email
      │
      ▼
Send Email via Gmail SMTP
```

---

## Example Response

```json
{
  "uploaded": "Resume Uploaded Successfully",
  "candidate_email": "candidate@example.com",
  "subject": "Application Update",
  "body": "Thank you for applying..."
}
```


## Author

**Mudit Joshi**

Learning AI Automation using Python & FastAPI.
