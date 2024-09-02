FROM python:3.7.3-slim

COPY requirements.txt /

RUN pip3 install --upgrade pip

RUN pip3 install -r /requirements.txt



COPY . /app

WORKDIR /app



EXPOSE 8080



CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]


# Base Image
#FROM python:3.9-slim

# Work directory
#WORKDIR /app

# Copy requirements and install dependencies
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt

# Copy other project files
#COPY . .

# Expose a port to Containers 
#EXPOSE 8080

# Command to run on server
#CMD gunicorn app:app & python3 bot.py


#FROM python:3.10.8-slim-buster
#WORKDIR /app

#COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt

#COPY . .

#CMD gunicorn app:app & python3 bot.py
