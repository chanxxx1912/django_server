# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the working directory
COPY . /app

# Install the required dependencies
#RUN pip3 install -r requirements.txt

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . . 

# Set the environment variables
ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Expose the default Django port
EXPOSE 8000

# Define the default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

