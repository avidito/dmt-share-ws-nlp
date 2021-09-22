FROM python:3.9-slim-buster
RUN apt-get update -y && \
    apt-get install -y wget gnupg gnupg2 gnupg1 && \
    apt-get install -y vim && \
    apt-get install -y unzip && \
    apt-get install -y cron

########## Setting up Google Chrome for Selenium ##########
# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
RUN apt-get install -y google-chrome-stable

########## Setting up Web Scraper Project ##########
COPY . /home/scraper
WORKDIR /home/scraper

# Remove unnecessary files/directory
RUN rm Dockerfile
RUN rm shared/chromedriver.exe
RUN rm -rf result/
RUN rm -rf *-env/
RUN find . -type d -name '__pycache__' -exec rm -r {} \; -prune

# Install python libraries
RUN pip install -r requirements.txt

# Donwload and unzip Chromedriver (using version 93.0.4577.63 for Chromer version 93)
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/93.0.4577.63/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable
ENV DISPLAY=:99

# Create Dummy Test script
RUN touch test.py
RUN echo 'import time; time.sleep(1000)' > test.py

# Set command
CMD ["python", "test.py"]
