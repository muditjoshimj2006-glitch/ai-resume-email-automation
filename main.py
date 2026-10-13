from fastapi import FastAPI
from app.router.email import router

app = FastAPI()
app.include_router(router)

#decorator
@app.get("/")
def greet():
    return{
        "message" : "Welcome To The AI Email Automation System"
    }

