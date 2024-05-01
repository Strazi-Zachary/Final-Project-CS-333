FROM python:3.8

WORKDIR /app

COPY . /app/

ADD requirements.txt .

ADD contacts.txt .

RUN pip install -r requirements.txt

CMD ["python3", "./Main.py"]