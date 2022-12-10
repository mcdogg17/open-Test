FROM python:latest

RUN pip install --upgrade pip

COPY . .

EXPOSE 80:80

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]