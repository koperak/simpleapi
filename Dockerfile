FROM python:3.9-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY . /code
EXPOSE 5000
CMD ["flask", "run"]