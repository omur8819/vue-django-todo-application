FROM python:3.10-alpine3.15

RUN pip install --upgrade pip

RUN adduser --disabled-password --gecos '' myuser

COPY ./vuengo/requirements.txt .
RUN pip install -r requirements.txt

COPY ./vuengo /app

WORKDIR /app

COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]