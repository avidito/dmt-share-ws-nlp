DELETE FROM ws.scraping_result src_tbl
WHERE (
  SELECT *
  FROM cdc.scraping_result cdc_tbl
  WHERE src_tbl.title = cdc_tbl.title
);

INSERT INTO ws.scraping_result
SELECT
  *,
  CURRENT_TIMESTAMP AS load_dt
FROM cdc.scraping_result;

TRUNCATE TABLE cdc.scraping_result;
