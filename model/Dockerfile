FROM python:3.11-slim

WORKDIR /app

COPY ../software/requirements.txt .

RUN python3 -m venv venv && ./venv/bin/pip install --upgrade pip && ./venv/bin/pip install -r requirements.txt

COPY train_model.py .

CMD ["./venv/bin/python", "train_model.py"]
