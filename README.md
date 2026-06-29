# Job Market Intelligence

Job Market Intelligence is an AI-assisted analytics case study for tracking hiring demand, skill trends, salary signals, and role-level market movement.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Skill%20Extraction-blueviolet?style=flat-square)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)

## Executive Summary

Students, job seekers, and workforce teams need to understand which roles are growing, which skills are requested most often, and where salary opportunities are strongest. Job listings contain these signals, but they are usually unstructured and hard to compare.

This project turns job-posting records into a structured intelligence layer using keyword extraction, SQL analytics, and dashboard-ready market indicators.

## Key Features

- Skill-demand extraction from job descriptions.
- Role and location trend analysis.
- Salary band comparison across roles.
- SQL reporting views for market intelligence dashboards.
- Python workflow for repeatable job-posting enrichment.

## Architecture Pipeline

```text
Job postings
    -> Text cleaning and skill extraction
    -> Role, location, and salary normalization
    -> Market KPI table
    -> SQL trend reporting
    -> Dashboard and career recommendations
```

## Repository Structure

```text
Job-Market-Intelligence/
├── data/
│   └── sample_job_posts.csv
├── docs/
│   ├── dashboard_blueprint.md
│   └── market_insights.md
├── scripts/
│   └── skill_demand_analysis.py
├── sql/
│   └── job_market_queries.sql
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Actionable Insights Demonstrated

- Python, SQL, Power BI, and machine learning signals can be used to compare role readiness.
- Salary ranges should be reviewed with role family and location together, not in isolation.
- Skill-frequency reporting helps learners prioritize the most market-relevant tools.
- Hiring trend dashboards can support placement teams, colleges, and career coaches.

## How To Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the skill-demand analysis:

```bash
python scripts/skill_demand_analysis.py
```

3. Review the generated output:

```text
data/skill_demand_output.csv
```

4. Use `sql/job_market_queries.sql` to build reporting views for dashboards.

## Suggested GitHub Topics

`job-market-analytics`, `workforce-analytics`, `skill-extraction`, `nlp`, `data-analytics`, `business-intelligence`, `powerbi-dashboard`, `sql`, `python`, `pandas`, `machine-learning`, `portfolio-project`
