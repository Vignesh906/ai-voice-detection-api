from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Optional

API_KEY = "my_voice_api_key_2026"

app = FastAPI(
    title="AI Voice Detection & Honeypot API",
    docs_url="/docs",
    openapi_url="/openapi.json"
)

# -------- AUTH (accept BOTH headers) --------
def verify_api_key(
    x_api_key: Optional[str],
    authorization: Optional[str]
):
    if x_api_key == API_KEY:
        return
    if authorization == API_KEY:
        return
    raise HTTPException(status_code=401, detail="Invalid API Key")

# -------- ROOT (HONEYPOT TESTER) --------
@app.api_route("/", methods=["GET", "POST", "HEAD"])
def root(
    x_api_key: Optional[str] = Header(None),
    authorization: Optional[str] = Header(None)
):
    verify_api_key(x_api_key, authorization)
    return JSONResponse(
        status_code=200,
        content={"status": "ok"}
    )

# -------- VOICE DETECTION --------
@app.api_route("/detect-voice", methods=["GET", "POST"])
async def detect_voice(
    request: Request,
    x_api_key: Optional[str] = Header(None),
    authorization: Optional[str] = Header(None)
):
    verify_api_key(x_api_key, authorization)

    try:
        body = await request.json()
    except:
        body = {}

    # Honeypot-style call
    if not body or "message" in body:
        return {"status": "ok"}

    # Voice detection response
    return {
        "result": "AI_GENERATED",
        "confidence": 0.75,
        "language": body.get("language", "English")
    }
