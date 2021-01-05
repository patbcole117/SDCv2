FROM python:alpine3.7
COPY . /sdc
WORKDIR /sdc
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2
RUN pip install -r requirements.txt
RUN pip install gunicorn
CMD [ "gunicorn", "--workers", "1", "--bind", "0.0.0.0:80", "run:app" ]