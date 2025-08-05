FROM python:3.11-slim

WORKDIR /app

# Create the data directory
RUN mkdir -p /app/data

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run app.py instead of the FastAPI server
CMD ["python", "app.py"]
