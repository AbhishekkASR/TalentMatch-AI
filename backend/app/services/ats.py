from app.services.skills import extract_skills


def calculate_ats_score(resume_text: str, job_description: str = ""):

    score = 0

    resume_text = resume_text.lower()

    # SECTION CHECKS
    sections = [
        "skills",
        "experience",
        "education",
        "project",
        "certification"
    ]

    found_sections = 0

    for section in sections:

        if section in resume_text:
            found_sections += 1

    structure_score = found_sections / len(sections)

    # SKILL MATCH
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    if jd_skills:

        matched = [
            s for s in jd_skills
            if s in resume_skills
        ]

        skill_score = len(matched) / len(jd_skills)

    else:
        skill_score = 0.5

    # LENGTH CHECK
    word_count = len(resume_text.split())

    if 300 <= word_count <= 1200:
        readability_score = 1.0
    else:
        readability_score = 0.5

    final_score = (
        0.4 * structure_score +
        0.4 * skill_score +
        0.2 * readability_score
    )

    return round(final_score, 2)