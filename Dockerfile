FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN pip install -U pip
COPY requirements.txt .
RUN pip install -r requirements.txt