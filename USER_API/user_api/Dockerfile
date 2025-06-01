FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn mysql-connector-python
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]
