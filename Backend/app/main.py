from fastapi import FastAPI

app = FastAPI(
title="Sentinel AI",
version ="1.0.0",
description="Enterprise Intelligence & Fraud Analytics Platform"
)

@app.get("/")
def root():
    return {
        "message": "Sentinel AI is running."
    }
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

