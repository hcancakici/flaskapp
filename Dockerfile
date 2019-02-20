FROM python:3.5-alpine

MAINTAINER H. Can Çakıcı <can.cakici@metglobal.com>

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 8080

ENV PORT 8080

CMD ["python3", "main.py"]
