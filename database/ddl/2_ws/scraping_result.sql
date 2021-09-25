DROP TABLE IF EXISTS ws.scraping_result;

CREATE TABLE ws.scraping_result (
  title VARCHAR PRIMARY KEY,
  website VARCHAR,
  channel VARCHAR,
  category VARCHAR,
  native_category VARCHAR,
  url VARCHAR,
  publish_dt TIMESTAMP,
  load_dt TIMESTAMP
);
