DROP TABLE IF EXISTS cdc.scraping_result;

CREATE TABLE cdc.scraping_result (
  title VARCHAR PRIMARY KEY,
  website VARCHAR,
  channel VARCHAR,
  category VARCHAR,
  native_category VARCHAR,
  url VARCHAR
);
