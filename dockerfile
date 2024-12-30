# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y libpq-dev

# Copy the requirements.txt file into the container and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your Django project files into the container
COPY . /app/

# Collect static files (for serving static content)
RUN python manage.py collectstatic --noinput

# Expose the port that Gunicorn will run on
EXPOSE 8000

# Start the Gunicorn server
CMD ["gunicorn", "phonemarketplace.wsgi:application", "--bind", "0.0.0.0:8000"]
