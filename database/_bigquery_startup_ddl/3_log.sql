DROP TABLE IF EXISTS log.job_scraping;

CREATE TABLE log.job_scraping (
  job_id STRING,
  rowcount INT64,
  duration INT64,
  load_dt DATETIME
);
