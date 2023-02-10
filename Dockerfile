# Specify python version
FROM python:3.9
# To see the python command on terminal
ENV PYTHONUNBUFFERED 1
# Create working directory
WORKDIR /app
# Copy requirements file to app file
COPY requirements.txt /app/requirements.txt
# Installing the required library
RUN pip install -r requirements.txt
# Copy all the necessary file and folder to app directory
COPY . /app
# Run the project
CMD python manage.py runserver 0.0.0.0:8000