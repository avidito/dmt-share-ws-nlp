DROP TABLE IF EXISTS cdc.job_scraping;

CREATE TABLE cdc.job_scraping (
  job_id VARCHAR,
  rowcount INTEGER,
  duration INTEGER
);
