# Pull base image
FROM python:3.9-slim

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /src

# Install dependencies
COPY . .
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000
