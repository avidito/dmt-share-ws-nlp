DROP TABLE IF EXISTS cdc.job_scraping;

CREATE TABLE cdc.job_scraping (
  job_id VARCHAR,
  rowcount INTEGER,
  duration INTEGER
);

DROP TABLE IF EXISTS cdc.scraping_result;

CREATE TABLE cdc.scraping_result (
  title VARCHAR,
  website VARCHAR,
  channel VARCHAR,
  category VARCHAR,
  native_category VARCHAR,
  url VARCHAR,
  publish_dt TIMESTAMP
);
