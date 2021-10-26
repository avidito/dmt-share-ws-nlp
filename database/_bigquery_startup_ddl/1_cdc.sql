DROP TABLE IF EXISTS cdc.job_scraping;

CREATE EXTERNAL TABLE cdc.job_scraping (
  job_id STRING,
  rowcount INT64,
  duration INT64
)
OPTIONS (
  FORMAT = "NEWLINE_DELIMITED_JSON",
  URIS = ["gs://dmt_share_leorio/src/job/job_scraping_*.json"]
);

DROP TABLE IF EXISTS cdc.scraping_result;

CREATE EXTERNAL TABLE cdc.scraping_result (
  title STRING,
  website STRING,
  channel STRING,
  category STRING,
  native_category STRING,
  url STRING,
  publish_dt DATETIME
)
OPTIONS (
  FORMAT = "NEWLINE_DELIMITED_JSON",
  URIS = ["gs://dmt_share_leorio/src/scraping_result/*.json"]
);
