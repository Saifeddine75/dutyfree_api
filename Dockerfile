FROM python:3.10-slim-buster
RUN pip install --no-cache-dir -r requirements.txt
ADD . /src/dutyfree_api
WORKDIR /src/dutyfree_api/dutyfree_api
CMD [ "python", "manage.py", "runserver" ]

