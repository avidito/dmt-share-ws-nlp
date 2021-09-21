DROP TABLE IF EXISTS log.job_scraping;

CREATE TABLE log.job_scraping (
  job_id VARCHAR,
  rowcount INTEGER,
  duration INTEGER,
  load_dt TIMESTAMP
);
