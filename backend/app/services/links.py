def clean_role(role: str) -> str:
    role = role.lower().strip()
    role = role.replace("/", " ")
    role = role.replace(",", " ")
    role = role.replace("&", " ")
    role = " ".join(role.split())
    return role


def format_dash(role: str) -> str:
    return clean_role(role).replace(" ", "-")


def format_plus(role: str) -> str:
    return clean_role(role).replace(" ", "+")


def generate_job_links(role: str):
    dash_role = format_dash(role)
    plus_role = format_plus(role)

    return {
        "naukri": f"https://www.naukri.com/{dash_role}-jobs",
        "linkedin": f"https://www.linkedin.com/jobs/search/?keywords={plus_role}",
        "indeed": f"https://www.indeed.com/jobs?q={plus_role}",
    }