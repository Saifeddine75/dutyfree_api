FROM python:3.10-slim-buster
ADD . .
WORKDIR /
RUN pip install --no-cache-dir -r requirements.txt
ENV HEARTBEAT_CHECK_INTERVAL=3600s
CMD [ "python", "manage.py", "runserver" ]
