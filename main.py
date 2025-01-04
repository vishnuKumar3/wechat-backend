from fastapi import FastAPI
from routes.rag import (router as rag_router)
from routes.topics import (router as topics_router)
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app=FastAPI()
app.include_router(rag_router)
app.include_router(topics_router)
origins = [
    "http://localhost:5173",
    "https://wechat-react.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    return {"status":"success"}
