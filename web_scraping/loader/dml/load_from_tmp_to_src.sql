-- Delete duplicate data between tmp and src table
DELETE FROM ws.scraping_result src_tbl
WHERE EXISTS (
  SELECT *
  FROM tmp.scraping_result tmp_tbl
  WHERE src_tbl.title = tmp_tbl.title
);

-- Insert data to tmp table
INSERT INTO ws.scraping_result
SELECT
  *,
  CURRENT_DATETIME("Asia/Jakarta") AS load_dt
FROM tmp.scraping_result;
