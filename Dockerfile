FROM python:3.8

WORKDIR /mnt/c/Users/zstra/OneDrive/Documents/Cs 333/Final_Project_CS333/Final-Project-CS-333/Main.py

COPY . /mnt/c/Users/zstra/OneDrive/Documents/Cs 333/Final_Project_CS333/Final-Project-CS-333/

ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3", "Main.py"]