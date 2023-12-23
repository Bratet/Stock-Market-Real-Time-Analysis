FROM python:3.9-slim

COPY requirements.txt /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/

# EXPOSE 5000

# CMD ["python", "main.py"]
