# Start with the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies for PostgreSQL and MySQL (adjust as needed)
RUN apt-get update && apt-get install -y libpq-dev gcc default-libmysqlclient-dev

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the entire Django project into the container
COPY . .

# Run migrations and collect static files if needed
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# Expose the port and run the application
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "nightlife.wsgi:application"]
