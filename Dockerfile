# FROM python:3.11-slim

# WORKDIR /app

# COPY . /app

# RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 9090

# CMD ["python", "app.py"]

FROM python:3.9-slim
# Install sh or bash
RUN apt-get update && apt-get install -y bash
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

