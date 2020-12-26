FROM python:alpine3.7
COPY . /SDC
WORKDIR /SDC
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2
RUN pip install -r requirements.txt
EXPOSE 50200
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]