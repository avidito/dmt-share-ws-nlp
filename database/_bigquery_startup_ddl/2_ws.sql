DROP TABLE IF EXISTS ws.scraping_result;

CREATE TABLE ws.scraping_result (
  title STRING,
  website STRING,
  channel STRING,
  category STRING,
  native_category STRING,
  url STRING,
  publish_dt DATETIME,
  load_dt DATETIME
);
