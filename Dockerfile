FROM python:3.5

MAINTAINER Andre Naleavaiko <andre@gorillascode.com>

ADD . /church-api

RUN mkdir -p /church-api/logs

WORKDIR /church-api

RUN pip install --upgrade pip
RUN pip install gunicorn eventlet
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--config=gunicorn.py", "run:app"]
