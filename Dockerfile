FROM python:3.8.3-slim-buster
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app


COPY /requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD ["python", "main.py"]
