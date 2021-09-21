FROM python:3.9-slim-buster
RUN apt-get update -y && \
    apt-get -y install cron

# Set working directory
WORKDIR /home/scraper

# Install python libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project content
COPY scraper/ scraper/
COPY shared/ shared/
COPY run.py .
COPY config.json .

# Test script
RUN touch test.py
RUN echo 'import time; time.sleep(1000)' > test.py

# Set command
CMD ["python", "test.py"]
