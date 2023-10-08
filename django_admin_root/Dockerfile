FROM python:3.11

ENV PYTHONUNBUFFERED 1
# allows output of the application (e.g. Django logs) to be seen in real-time
# ensure that the Python output is sent straight to the terminal without being first buffered, 
# which allows for real-time viewing of the application output 
# and prevents partial output from being lost in case of a crash.

WORKDIR /django_admin_root
# create a new dir /django_admin_root

COPY ./requirements.txt /django_admin_root/requirements.txt
# req.txt is next to Dockerfile, so copy that into /django_admin_root

RUN pip install --no-cache-dir --upgrade -r /django_admin_root/requirements.txt

COPY ./django_admin /django_admin_root/django_admin