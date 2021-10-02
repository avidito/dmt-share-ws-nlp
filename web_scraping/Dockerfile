FROM python:3.9-slim-buster

RUN apt-get update -y && \
    apt-get install -y wget gnupg gnupg2 gnupg1 && \
    apt-get install -y unzip && \
    apt-get install -y cron && \
    apt-get install -y postgresql-client && \
    apt-get install -y vim

########## Setup Scraper Project ##########
COPY . /app/web_scraping
WORKDIR /app/web_scraping
RUN mkdir /logs/
RUN mkdir /backup/
RUN mkdir /backup/scraping_result/
RUN rm Dockerfile
RUN rm scraper/chromedriver.exe
RUN rm -rf result/
RUN rm -rf *-env/
RUN find . -type d -name '__pycache__' -exec rm -r {} \; -prune

ENV PROJECT_DIR=/app/web_scraping
ENV RESULT_DIR=/app/web_scraping/result
ENV BACKUP_DIR=/backup

RUN pip install --default-timeout=100 -r requirements.txt
RUN crontab schedule.txt

########## Setup Selenium with Google Chrome ##########
# Add Google Chrome Repository
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Install Google Chrome
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# Setup Chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/93.0.4577.63/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
ENV DISPLAY=:99

########## Keep Container Running ##########
CMD ["tail", "-f", "/dev/null"]
