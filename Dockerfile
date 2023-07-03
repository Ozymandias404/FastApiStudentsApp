FROM python:3.9-bookworm

LABEL title="A containerized FastApi App"

RUN mkdir -p /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN python3 -m pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "controllers.main:app", "--host", "0.0.0.0", "--port", "80"]

