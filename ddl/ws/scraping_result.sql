DROP TABLE IF EXISTS ws.scraping_result;

CREATE TABLE ws.scraping_result (
  tilte VARCHAR PRIMARY KEY,
  website VARCHAR,
  channel VARCHAR,
  category VARCHAR,
  native_category VARCHAR,
  url VARCHAR,
  load_dt TIMESTAMP
);
