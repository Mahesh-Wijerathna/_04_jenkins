FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv venv && ./venv/bin/pip install --upgrade pip && ./venv/bin/pip install -r requirements.txt

COPY app.py .

CMD ["./venv/bin/python", "app.py"]
