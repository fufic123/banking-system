FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for psycopg2 and Postgres client
RUN apt-get update && apt-get install -y libpq-dev gcc postgresql-client && rm -rf /var/lib/apt/lists/*

# Copy and install requirements
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and SQL scripts
COPY backend/app /app
COPY sql /app/sql

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose the FastAPI default port
EXPOSE 8000

# Default command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
