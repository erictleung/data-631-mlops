FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Install Python tools
RUN pip install uv dagster dagster-webserver mlflow
