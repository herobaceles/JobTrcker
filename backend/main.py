<<<<<<< HEAD
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google.oauth2 import id_token
from google.auth.transport import requests
from dotenv import load_dotenv
from pathlib import Path
import os

# Load environment variables
load_dotenv(Path(__file__).parent / ".env")
FRONTEND_URL = os.getenv("FRONTEND_URL")
app = FastAPI()

=======
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import ping_database
from routers import auth, application
from routers import application, calendar  # Import your new module
FRONTEND_URL = os.getenv("FRONTEND_URL")

app = FastAPI(title="Job Tracker Hub API Engine")

# CORS Policy Rules
>>>>>>> ea4caaf (Initial commit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

print("BACKEND GOOGLE_CLIENT_ID =", GOOGLE_CLIENT_ID)
print("BACKEND GOOGLE_CLIENT_ID =", repr(GOOGLE_CLIENT_ID))
print("FRONTEND URL= ", FRONTEND_URL)
class TokenPayload(BaseModel):
    token: str


@app.post("/api/auth/google")
def verify_google_token(payload: TokenPayload):
    try:
        # Verify Google ID token
        id_info = id_token.verify_oauth2_token(
            payload.token,
            requests.Request(),
            GOOGLE_CLIENT_ID,
        )

        # Debug information
        print("=== GOOGLE TOKEN VERIFIED ===")
        print("NAME :", id_info.get("name"))
        print("EMAIL:", id_info.get("email"))
        print("AUD  :", id_info.get("aud"))
        print("SUB  :", id_info.get("sub"))
        print("============================")

        user_name = id_info.get("name")

        return {
            "status": "success",
            "message": f"Successfully verified {user_name} on Python backend.",
        }

    except Exception as e:
        print("=== GOOGLE TOKEN ERROR ===")
        print(str(e))
        print("==========================")

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
=======
app.include_router(application.router)
app.include_router(calendar.router)
# Lifespan Hook Verification Check
@app.on_event("startup")
async def startup_db_client():
    try:
        await ping_database()
        print("Successfully connected to MongoDB asynchronously via config initialization!")
    except Exception as e:
        print(f"Could not connect to MongoDB: {e}")

# Register and Mount Modular Domain Routers
app.include_router(auth.router)
app.include_router(application.router)
>>>>>>> ea4caaf (Initial commit)
