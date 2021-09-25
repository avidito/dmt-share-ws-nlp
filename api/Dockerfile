FROM python:3.9-slim-buster

RUN apt-get update -y

########## Setting up API Project ##########
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
