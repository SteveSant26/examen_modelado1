FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 7777

CMD ["python", "main.py"]
