FROM python:3.11

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
