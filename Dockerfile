FROM  python:3.8-slim

WORKDIR /todo

ADD . /todo

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python todo/manage.py runserver 0:8000
