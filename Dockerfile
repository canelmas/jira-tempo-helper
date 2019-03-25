FROM python:3.7

LABEL maintainer="Can Elmas can@commencis.com"

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD python jira-tempo-helper.py

EXPOSE 5000
