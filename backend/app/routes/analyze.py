from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.services.parser import extract_text_from_file

from app.services.matcher import (
    analyze_resume_job,
    recommend_roles,
    load_naukri_roles
)

router = APIRouter()

@router.post("/analyze_resume")
async def analyze_resume(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        file_bytes = await resume_file.read()

        resume_text = extract_text_from_file(
            resume_file.filename,
            file_bytes
        )

        if not resume_text.strip():
            return {
                "match_percentage": 0,
                "decision": "Could not extract readable text from the resume",
                "matched_skills": [],
                "missing_skills": [],
                "ats_score": 0,
                "improvement_suggestions": [
                    "Use a text-based PDF or a clearer image",
                    "Ensure the resume is readable",
                    "Try again with a better scan"
                ],
                "recommended_roles": []
            }

        # MAIN ANALYSIS
        result = analyze_resume_job(
            resume_text,
            job_description
        )

        # ROLE RECOMMENDATIONS
        role_profiles = load_naukri_roles()
        recommended_roles = recommend_roles(
            resume_text,
            role_profiles
        )

        result["recommended_roles"] = recommended_roles

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )