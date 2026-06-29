"""NLP-style skill demand analysis for synthetic Indian job market postings."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "sample_job_posts.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "skill_demand_output.csv"
SKILLS: Dict[str, List[str]] = {
    "Python": ["python"],
    "SQL": ["sql"],
    "Power BI": ["power bi", "dax"],
    "Tableau": ["tableau"],
    "Excel": ["excel"],
    "Machine Learning": ["machine learning", "scikit-learn"],
    "NLP": ["nlp"],
    "Forecasting": ["forecasting"],
}
ROLE_KEYWORDS = ["Data Analyst", "ML Engineer", "BI Developer", "AI Analyst", "Business Analyst", "Data Scientist"]


def load_jobs(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load job posts with date parsing and schema validation."""
    try:
        jobs = pd.read_csv(path, parse_dates=["posted_date"])
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Job posting file not found: {path}") from exc
    required = {"job_id", "title", "company", "location", "salary_min", "salary_max", "description", "posted_date"}
    missing = required.difference(jobs.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return jobs


def categorize_role(title: str) -> str:
    """Map a title to a normalized role category."""
    for role in ROLE_KEYWORDS:
        if role.lower() in title.lower():
            return role
    return "Other"


def extract_skills(description: str) -> List[str]:
    """Extract skills using transparent keyword matching."""
    normalized = description.lower()
    matched: List[str] = []
    for skill, keywords in SKILLS.items():
        # Multiple aliases allow DAX to count as Power BI demand.
        if any(keyword in normalized for keyword in keywords):
            matched.append(skill)
    return matched


def build_skill_output(jobs: pd.DataFrame) -> pd.DataFrame:
    """Count skill frequency per role category and attach salary statistics."""
    enriched = jobs.copy()
    enriched["role_category"] = enriched["title"].apply(categorize_role)
    # Skills remain multi-label because one posting can demand SQL, BI, and ML together.
    enriched["skills"] = enriched["description"].apply(extract_skills)
    exploded = enriched.explode("skills").dropna(subset=["skills"])
    salary_stats = enriched.groupby("role_category", as_index=False).agg(
        avg_salary_min=("salary_min", "mean"),
        avg_salary_max=("salary_max", "mean"),
        postings=("job_id", "count"),
    )
    frequency = exploded.groupby(["role_category", "skills"], as_index=False).agg(skill_mentions=("job_id", "count"))
    output = frequency.merge(salary_stats, on="role_category", how="left")
    # Sorting makes the console output immediately useful for recruiters.
    output = output.sort_values(["skill_mentions", "avg_salary_max"], ascending=[False, False])
    output[["avg_salary_min", "avg_salary_max"]] = output[["avg_salary_min", "avg_salary_max"]].round(0).astype(int)
    return output


def main() -> None:
    """Run the complete job-market intelligence pipeline."""
    jobs = load_jobs()
    output = build_skill_output(jobs)
    output.to_csv(OUTPUT_PATH, index=False)
    summary = output.groupby("skills", as_index=False)["skill_mentions"].sum().sort_values("skill_mentions", ascending=False).head(5)
    print("Top 5 skill demand summary")
    print(summary.to_string(index=False))
    print(f"Rows processed: {len(jobs)}")
    print(f"Output: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
