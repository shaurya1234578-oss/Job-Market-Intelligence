# Job Market Intelligence

NLP-style batch analytics pipeline for skill demand, hiring trends, salary ranges, and role demand across Indian analytics job postings.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)

## Executive Summary

This project analyzes 150 synthetic job postings across Noida, Gurugram, Delhi, Bengaluru, Hyderabad, and Mumbai. It extracts skills from job descriptions, groups demand by role category, computes salary statistics, and creates SQL-ready outputs for workforce intelligence dashboards.

## Insights

### Top 5 Skills In Demand

| Skill | Mentions |
|---|---:|
| SQL | 150 |
| Python | 100 |
| Power BI | 75 |
| Machine Learning | 75 |
| NLP | 75 |

### Average Salary By Role

| Role | Avg Salary Min | Avg Salary Max |
|---|---:|---:|
| Data Scientist | ₹930,000 | ₹1,280,000 |
| ML Engineer | ₹880,000 | ₹1,163,333 |
| AI Analyst | ₹780,000 | ₹1,063,333 |
| BI Developer | ₹680,000 | ₹1,030,000 |
| Business Analyst | ₹580,000 | ₹880,000 |
| Data Analyst | ₹530,000 | ₹780,000 |

## How To Run

```bash
pip install -r requirements.txt
python scripts/skill_demand_analysis.py
```

Expected terminal output:

```text
Top 5 skill demand summary
           skills  skill_mentions
              SQL             150
           Python             100
         Power BI              75
 Machine Learning              75
              NLP              75
Rows processed: 150
Output: data/skill_demand_output.csv
```

## Architecture Pipeline

```text
Synthetic job postings
    -> Keyword skill extraction
    -> Role category normalization
    -> Skill frequency and salary statistics
    -> SQL market intelligence queries
    -> Dashboard-ready workforce insights
```
