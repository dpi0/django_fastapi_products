FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /fastapi_main_root
# create a new dir /fastapi_main_root

COPY ./requirements.txt /fastapi_main_root/requirements.txt
# req.txt is next to Dockerfile, so copy that into /fastapi_main_root

RUN pip install --no-cache-dir --upgrade -r /fastapi_main_root/requirements.txt

COPY ./app /fastapi_main_root/app
