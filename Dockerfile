FROM python:3

WORKDIR /app

COPY . /app

ENV FLASK_APP=app.py

ENV FLASK_ENV=development

ENV FLASK_RUN_HOST=0.0.0.0

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["flask", "run"]
