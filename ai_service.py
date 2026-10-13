#LLM CALLING
from dotenv import load_dotenv
from google import genai
from app.config import api_key


load_dotenv()

def resume_analysis(text):
 try:
    client = genai.Client(api_key=api_key)

    prompt = f"""From the give {text} write a professional email by understanding these things
    1. it should me clear and simple
    2. make it professional
    3. don't make it too long or too short
    4. If the resume contains a name and email, use the uplaoded resume {text} of user and highlight his name and email 
    5. use professional formating
    6. analysis the full resume and take decision of hiring a candidate based on his / her resume quality
    7. so after point number 6 write an email for professionally reply them for (hiring or not hiring)
    8. Return ONLY valid JSON in this format:

{{
  "subject": "...",
  "body": "..."
}}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


 except Exception as e:
      print(f"ERROR : {e}")
      None