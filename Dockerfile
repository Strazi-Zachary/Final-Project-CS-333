FROM python:3.8

WORKDIR /app

COPY . /app/

ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3", "Main.py"]