import re

SKILL_LIST = [
    "python", "java", "javascript", "typescript", "sql", "html", "css",
    "react", "angular", "vue", "node", "express", "fastapi", "django",
    "flask", "mongodb", "postgresql", "mysql", "aws", "azure", "gcp",
    "docker", "kubernetes", "git", "github", "linux",
    "machine learning", "deep learning", "ai", "nlp",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "excel", "power bi", "tableau", "data analysis",
    "api", "rest api", "testing", "manual testing", "automation testing",
    "communication", "problem solving", "debugging", "agile"
]


def extract_skills(text: str, skill_list=None):
    if skill_list is None:
        skill_list = SKILL_LIST

    cleaned = text.lower()
    found = []

    for skill in sorted(skill_list, key=len, reverse=True):
        if re.search(re.escape(skill.lower()), cleaned):
            found.append(skill)

    deduped = []
    seen = set()
    for skill in found:
        if skill not in seen:
            deduped.append(skill)
            seen.add(skill)

    return deduped