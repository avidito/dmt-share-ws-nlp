-- Drop tmp table
DROP TABLE IF EXISTS tmp.scraping_result;

-- Crate table without duplicate data
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

-- Re-populate cdc table with clean data
TRUNCATE TABLE cdc.scraping_result;

INSERT INTO cdc.scraping_result
SELECT * FROM tmp.scraping_result;
