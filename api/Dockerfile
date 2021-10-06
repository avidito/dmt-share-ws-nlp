FROM python:3.8.3-slim-buster

RUN apt-get update -y && \
    apt-get install -y gcc musl-dev && \
    apt-get install -y build-essential && \
    apt-get install -y python-dev python3-dev && \
    apt-get install -y libpq-dev

########## Setting up API Project ##########
ENV TZ=Asia/Jakarta
COPY . /app/api/
WORKDIR /app/api/

# Remove unnecessary files/directory
RUN rm Dockerfile
RUN rm -rf *-env/
RUN find . -type d -name '__pycache__' -exec rm -r {} \; -prune

# Install python libraries
RUN pip install -r requirements.txt

# Set command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
