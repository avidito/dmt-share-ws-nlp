-- Delete duplicate data between cdc and src table
DELETE FROM ws.scraping_result src_tbl
WHERE EXISTS (
  SELECT *
  FROM cdc.scraping_result cdc_tbl
  WHERE src_tbl.title = cdc_tbl.title
);

-- Insert data to src table
INSERT INTO ws.scraping_result
SELECT
  *,
  CURRENT_TIMESTAMP AS load_dt
FROM cdc.scraping_result;

-- Clean cdc table
TRUNCATE TABLE cdc.scraping_result;
