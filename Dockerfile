FROM python:3.8

MAINTAINER Andy Kim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements/ /app/requirements
RUN pip install --no-cache-dir -r requirements/requirements-dev.txt

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0:8000"]
