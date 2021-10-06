\copy cdc.scraping_result
FROM '{{result_dir}}scraping_result.csv'
DELIMITER ','
CSV HEADER;
