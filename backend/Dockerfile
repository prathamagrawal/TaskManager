FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
ENV PYTHONUNBUFFERED=1
RUN apt-get update -y
RUN apt-get install pkg-config -y
RUN apt-get install -y python3-dev build-essential
RUN apt-get install -y default-libmysqlclient-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
# CMD ["python","manage.py","runserver"]