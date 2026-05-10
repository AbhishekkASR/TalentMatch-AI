import pandas as pd
from functools import lru_cache

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.services.skills import extract_skills
from app.services.ats import calculate_ats_score
from app.services.links import generate_job_links


@lru_cache(maxsize=1)
def get_model():
    return SentenceTransformer("paraphrase-MiniLM-L3-v2")


def get_embedding(text: str):
    model = get_model()
    return model.encode(text)

def build_role_profiles_from_naukri(df):

    roles = []

    for _, row in df.iterrows():

        roles.append({

            "title": str(
                row.get("jobtitle", "")
            ).strip(),

            "skills": [
                s.strip()

                for s in str(
                    row.get("skills", "")
                ).lower().split(",")

                if s.strip()
            ],

            "description": str(
                row.get("jobdescription", "")
            ).strip(),

            "company": str(
                row.get("company", "")
            ).strip(),

            "location": str(
                row.get("joblocation", "")
            ).strip(),

            "industry": str(
                row.get("industry", "")
            ).strip(),

            "experience": str(
                row.get("experience", "")
            ).strip(),
        })

    return roles
def load_naukri_roles():

    df = pd.read_csv(
        "app/data/naukri_jobs.csv",
        encoding="utf-8",
        low_memory=False
    )

    df = df.sample(
        n=min(200, len(df)),
        random_state=42
    )

    roles = []

    for _, row in df.iterrows():

        skills = []

        raw_skills = str(
            row.get("skills", "")
        ).lower()

        for s in raw_skills.split(","):

            s = s.strip()

            if s:
                skills.append(s)

        roles.append({

            "title": str(
                row.get("jobtitle", "")
            ).strip(),

            "skills": skills,

            "description": str(
                row.get("jobdescription", "")
            ).strip(),

            "company": str(
                row.get("company", "")
            ).strip(),

            "location": str(
                row.get("joblocation", "")
            ).strip(),

            "industry": str(
                row.get("industry", "")
            ).strip(),

            "experience": str(
                row.get("experience", "")
            ).strip()
        })

    return roles

def analyze_resume_job(resume_text: str, job_description: str):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    resume_emb = get_embedding(resume_text)
    job_emb = get_embedding(job_description)

    semantic_similarity = cosine_similarity(
        [resume_emb],
        [job_emb]
    )[0][0]

    semantic_similarity = float(semantic_similarity)

    matched_skills = [
        skill for skill in job_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    skill_score = (
        len(matched_skills) / len(job_skills)
        if job_skills else 0.0
    )

    ats_score = float(
        calculate_ats_score(
            resume_text,
            job_description
        )
    )

    final_score = (
        0.60 * semantic_similarity +
        0.30 * skill_score +
        0.10 * ats_score
    )

    match_percentage = round(float(final_score * 100), 2)

    if match_percentage >= 80:
        decision = "High chance of selection"

    elif match_percentage >= 60:
        decision = "Moderate chance of selection"

    else:
        decision = "Low chance of selection"

    suggestions = [
        f"Add {skill} to your resume"
        for skill in missing_skills[:5]
    ]

    if ats_score < 0.75:
        suggestions.append(
            "Improve resume structure by adding Skills, Projects, Experience, and Education sections"
        )

    return {
        "match_percentage": float(match_percentage),
        "decision": decision,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "ats_score": float(round(ats_score * 100, 2)),
        "improvement_suggestions": list(suggestions),
    }


def recommend_roles(resume_text: str, role_profiles: list):
    resume_emb = get_embedding(resume_text)
    resume_skills = extract_skills(resume_text)

    results = []

    for role in role_profiles:
        role_text = (
            f'{role["title"]} '
            + " ".join(role["skills"])
            + " "
            + role.get("description", "")
        )

        role_emb = get_embedding(role_text)

        semantic_similarity = cosine_similarity([resume_emb], [role_emb])[0][0]
        semantic_similarity = float(semantic_similarity)

        skill_matches = [s for s in role["skills"] if s in resume_skills]
        skill_score = len(skill_matches) / max(1, len(role["skills"]))

        score = 0.70 * semantic_similarity + 0.30 * skill_score
        score_pct = float(round(score * 100, 2))

        results.append({
            "title": role["title"],
            "score": score_pct,
            "matched_skills": list(skill_matches[:10]),
            "job_links": generate_job_links(role["title"])
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:5]