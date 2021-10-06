FROM python:3.9-slim-buster

RUN apt-get update -y && \
    apt-get install -y wget gnupg gnupg2 gnupg1 && \
    apt-get install -y unzip && \
    apt-get install -y cron && \
    apt-get install -y postgresql-client && \
    apt-get install -y gcc musl-dev && \
    apt-get install -y build-essential && \
    apt-get install -y python3-lxml python-dev python3-dev && \
    apt-get install -y libxslt-dev libxml2-dev libffi-dev libssl-dev && \
    apt-get install -y chromium

########## Setup Scraper Project ##########
ENV TZ=Asia/Jakarta

WORKDIR /app/web_scraping
COPY scraper scraper/
COPY loader loader/
COPY job_web_scraping.sh .
COPY requirements.txt .
COPY schedule.txt .
RUN rm scraper/chromedriver.exe
RUN find . -type d -name '__pycache__' -exec rm -r {} \; -prune

RUN mkdir /logs/
RUN mkdir /backup/
RUN mkdir /backup/scraping_result/

ENV PROJECT_DIR=/app/web_scraping
ENV RESULT_DIR=/app/web_scraping/result
ENV BACKUP_DIR=/backup

RUN pip install -r requirements.txt
RUN crontab schedule.txt

########## Setup Selenium with Google Chrome ##########
RUN wget https://github.com/electron/electron/releases/download/v12.0.9/chromedriver-v12.0.9-linux-armv7l.zip
RUN unzip chromedriver-v9.0.2-linux-armv7l.zip -d chromedriver/
RUN mv chromedriver/chromedriver /usr/local/bin/
RUN rm chromedriver-v9.0.2-linux-armv7l.zip
RUN rm -rf chromedriver

########## Keep Container Running ##########
CMD ["tail", "-f", "/dev/null"]
