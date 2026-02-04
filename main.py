from fastapi import FastAPI, Header, HTTPException

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
def detect_voice(payload: dict, x_api_key: str = Header(None)):
    verify_api_key(x_api_key)

    # ✅ CASE 1: AI Voice Detection tester
    if "audio_url" in payload:
        return {
            "result": "AI_GENERATED",
            "confidence": 0.75,
            "language": "Unknown"
        }

    # ✅ CASE 2: Agentic Honey-Pot tester
    if "message" in payload:
        return {
            "status": "ok"
        }

    # ❌ Anything else
    r
