COPY cdc.scraping_result
FROM '/home/landing/scraping_result.csv'
DELIMITER ','
CSV HEADER;
