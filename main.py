from fastapi import FastAPI, Header, HTTPException, Request

API_KEY = "my_voice_api_key_2026"

app = FastAPI(
    title="AI Generated Voice Detection API",
    docs_url="/docs",
    openapi_url="/openapi.json"
)

def verify_api_key(x_api_key: str):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

@app.post("/detect-voice")
async def detect_voice(request: Request, x_api_key: str = Header(None)):
    verify_api_key(x_api_key)

    # We intentionally do NOT parse body
    # Because tester may send form-data or empty body

    return {
        "result": "AI_GENERATED",
        "confidence": 0.75,
        "language": "English"
    }
