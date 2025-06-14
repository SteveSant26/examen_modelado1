FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install uvicorn

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
