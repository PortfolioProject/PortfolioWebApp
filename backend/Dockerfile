FROM python:3

RUN mkdir /backend
WORKDIR /backend

COPY . .
EXPOSE 8000
RUN pip install -r requirements.txt

CMD gunicorn -w 4 app:app -b 0.0.0.0:8000