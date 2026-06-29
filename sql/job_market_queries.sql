/*
Project: Job Market Intelligence
Author: Shaurya Rajput
Date: 2026-06-29
Description: SQL analysis for skills, salaries, hiring trends, locations, role demand, and seniority distribution.
*/

-- Query 1: Rank skills by total mentions to prioritize learning roadmap decisions.
WITH skill_mentions AS (
    SELECT skills AS skill_name, SUM(skill_mentions) AS total_mentions
    FROM skill_demand
    GROUP BY skills
)
SELECT skill_name, total_mentions, RANK() OVER (ORDER BY total_mentions DESC) AS demand_rank
FROM skill_mentions;

-- Query 2: Compare salary ranges by normalized role category.
WITH salary_by_role AS (
    SELECT role_category, AVG(avg_salary_min) AS avg_min_salary, AVG(avg_salary_max) AS avg_max_salary
    FROM skill_demand
    GROUP BY role_category
)
SELECT role_category, avg_min_salary, avg_max_salary
FROM salary_by_role
ORDER BY avg_max_salary DESC;

-- Query 3: Track hiring trend by month for market momentum.
WITH monthly_hiring AS (
    SELECT DATE_TRUNC('month', posted_date) AS posting_month, COUNT(*) AS posting_count
    FROM job_posts
    GROUP BY DATE_TRUNC('month', posted_date)
)
SELECT posting_month, posting_count, LAG(posting_count) OVER (ORDER BY posting_month) AS previous_month_count
FROM monthly_hiring;

-- Query 4: Identify top hiring locations for NCR and India targeting.
WITH location_demand AS (
    SELECT location, COUNT(*) AS posting_count
    FROM job_posts
    GROUP BY location
)
SELECT location, posting_count, ROW_NUMBER() OVER (ORDER BY posting_count DESC) AS location_rank
FROM location_demand;

-- Query 5: Build a role demand index combining posting count and salary ceiling.
WITH role_index AS (
    SELECT
        role_category,
        COUNT(*) AS postings,
        AVG(salary_max) AS avg_salary_max
    FROM job_posts
    GROUP BY role_category
)
SELECT role_category, postings, avg_salary_max, postings * avg_salary_max AS role_demand_index
FROM role_index
ORDER BY role_demand_index DESC;

-- Query 6: Estimate seniority distribution from title keywords.
WITH seniority AS (
    SELECT
        CASE
            WHEN LOWER(title) LIKE '%intern%' THEN 'Intern'
            WHEN LOWER(title) LIKE '%junior%' THEN 'Junior'
            WHEN LOWER(title) LIKE '%associate%' THEN 'Associate'
            ELSE 'Entry Level'
        END AS seniority_level,
        job_id
    FROM job_posts
)
SELECT seniority_level, COUNT(*) AS postings, RANK() OVER (ORDER BY COUNT(*) DESC) AS seniority_rank
FROM seniority
GROUP BY seniority_level;
