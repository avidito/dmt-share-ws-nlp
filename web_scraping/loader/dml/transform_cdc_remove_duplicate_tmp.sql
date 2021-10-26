DROP TABLE IF EXISTS tmp.scraping_result;

CREATE TABLE tmp.scraping_result AS
WITH dup_check_tbl AS (
  SELECT
    *,
    ROW_NUMBER() OVER(PARTITION BY title) AS rownumber
  FROM cdc.scraping_result
)
SELECT
  title,
  website,
  channel,
  category,
  native_category,
  url,
  publish_dt
FROM dup_check_tbl
WHERE rownumber = 1;
