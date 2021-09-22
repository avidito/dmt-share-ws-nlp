COPY cdc.scraping_result
FROM '/home/landing/scraping_result-all.csv'
DELIMITER ','
CSV HEADER;
