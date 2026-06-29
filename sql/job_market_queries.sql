-- Job Market Intelligence reporting queries.

CREATE TABLE job_posts (
    job_id VARCHAR(20) PRIMARY KEY,
    role VARCHAR(100),
    company VARCHAR(120),
    location VARCHAR(80),
    salary_min INTEGER,
    salary_max INTEGER,
    description TEXT
);

CREATE TABLE skill_demand (
    skill VARCHAR(80),
    posting_count INTEGER,
    avg_salary_min INTEGER,
    avg_salary_max INTEGER
);

SELECT
    role,
    COUNT(*) AS postings,
    AVG(salary_min) AS avg_salary_min,
    AVG(salary_max) AS avg_salary_max
FROM job_posts
GROUP BY role
ORDER BY postings DESC, avg_salary_max DESC;

SELECT
    skill,
    posting_count,
    avg_salary_min,
    avg_salary_max
FROM skill_demand
ORDER BY posting_count DESC, avg_salary_max DESC;
