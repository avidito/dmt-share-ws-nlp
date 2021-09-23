COPY cdc.scraping_result
FROM '/app/web_scraping/result/scraping_result.csv'
DELIMITER ','
CSV HEADER;
