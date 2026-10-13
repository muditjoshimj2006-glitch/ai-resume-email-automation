from fastapi import File, UploadFile, APIRouter
import os
import shutil
import json

from app.services.ai_service import resume_analysis
from app.services.pdf_service import pdf_reader, extract_email
from app.services.email_service import send_email

router = APIRouter()


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Read PDF
    text = pdf_reader(file_path)

    # Extract email
    to_email = extract_email(text)
    if to_email is None:
       return {
         "error": "No email found in resume."
    }

    # AI Response
    resume = resume_analysis(text)

    if resume is None:
       return {
         "error": "Gemini API is busy. Please try again after a few minutes."
    }

    resume_data = json.loads(resume)


    # Send Email
    try:
     send_email(
        to_email,
        resume_data["subject"],
        resume_data["body"]
    )

    except Exception as e:
     return {
        "error": f"Email sending failed: {str(e)}"
    }

    finally:
     if os.path.exists(file_path):
       os.remove(file_path) 


    return {
        "uploaded": "Resume Uploaded Successfully",
        "candidate_email": to_email,
        "subject": resume_data["subject"],
        "body": resume_data["body"]
    }