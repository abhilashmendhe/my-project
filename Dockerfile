# Use an official Python base image
FROM python:3.11-slim

WORKDIR /app
COPY fibonacci.py .

CMD ["python", "fibonacci.py", "10"]