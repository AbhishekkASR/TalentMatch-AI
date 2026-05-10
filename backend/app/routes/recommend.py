import json
import os

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.parser import extract_text_from_file
from app.services.matcher import recommend_roles

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROLE_FILE = os.path.join(BASE_DIR, "data", "role_profiles.json")


def load_role_profiles():
    with open(ROLE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


@router.post("/recommend_roles")
async def recommend_roles_from_resume(
    resume_file: UploadFile = File(...)
):
    try:
        role_profiles = load_role_profiles()

        file_bytes = await resume_file.read()
        resume_text = extract_text_from_file(resume_file.filename, file_bytes)

        if not resume_text.strip():
            return {"roles": [], "message": "Could not extract readable text from the resume"}

        results = recommend_roles(resume_text, role_profiles)
        return {"roles": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))