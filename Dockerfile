From python:3.11.14-alpine3.23
WORKDIR /app
COPY calculator.py .
CMD ["python", "calculator.py"]
