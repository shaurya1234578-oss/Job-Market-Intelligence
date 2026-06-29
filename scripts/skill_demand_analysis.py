"""Skill-demand analysis workflow for the Job Market Intelligence project."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "sample_job_posts.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "skill_demand_output.csv"

SKILLS = [
    "python",
    "sql",
    "power bi",
    "tableau",
    "excel",
    "machine learning",
    "aws",
    "nlp",
    "dax",
    "etl",
]


def load_jobs(path: Path = INPUT_PATH) -> pd.DataFrame:
    """Load job posting records."""
    return pd.read_csv(path)


def extract_skills(description: str) -> list[str]:
    """Extract known portfolio skills from a job description."""
    normalized = description.lower()
    return [skill for skill in SKILLS if skill in normalized]


def build_skill_demand(jobs: pd.DataFrame) -> pd.DataFrame:
    """Create a skill-demand table from job descriptions."""
    enriched = jobs.copy()
    enriched["extracted_skills"] = enriched["description"].apply(extract_skills)
    skill_rows = enriched.explode("extracted_skills").dropna(subset=["extracted_skills"])
    demand = (
        skill_rows.groupby("extracted_skills")
        .agg(
            posting_count=("job_id", "count"),
            avg_salary_min=("salary_min", "mean"),
            avg_salary_max=("salary_max", "mean"),
        )
        .reset_index()
        .rename(columns={"extracted_skills": "skill"})
        .sort_values(["posting_count", "avg_salary_max"], ascending=[False, False])
    )
    demand["avg_salary_min"] = demand["avg_salary_min"].round(0).astype(int)
    demand["avg_salary_max"] = demand["avg_salary_max"].round(0).astype(int)
    return demand


def main() -> None:
    """Run the complete job-market intelligence workflow."""
    jobs = load_jobs()
    demand = build_skill_demand(jobs)
    demand.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved skill-demand output to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
