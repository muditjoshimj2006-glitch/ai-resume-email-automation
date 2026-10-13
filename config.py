from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv("API_KEY")
sender_email = os.getenv("SENDER_EMAIL")
app_password = os.getenv("APP_PASSWORD")