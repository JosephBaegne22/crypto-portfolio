from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine, Base
from . import models
from .routes import auth, portfolio

app = FastAPI(title="Crypto Portfolio API")

# 🔐 CORS — OBLIGATOIRE POUR NEXT.JS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(portfolio.router)

@app.get("/")
def root():
    return {"message": "API Crypto Portfolio opérationnelle"}
