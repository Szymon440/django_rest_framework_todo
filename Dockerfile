FROM python:latest
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY project /app

CMD ["python", "project/manage.py", "runserver", "0.0.0.0:8000"]