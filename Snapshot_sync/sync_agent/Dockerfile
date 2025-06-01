FROM python:3.11
WORKDIR /app
COPY sync.py .
RUN pip install mysql-connector-python schedule
CMD ["python", "sync.py"]
