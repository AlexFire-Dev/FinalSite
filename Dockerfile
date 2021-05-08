FROM python:3.8

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip3 install gunicorn
RUN pip3 install -r requirements.txt

COPY . .

CMD ["./start.sh"]