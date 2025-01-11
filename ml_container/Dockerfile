FROM python:3.9-slim-bullseye

WORKDIR /app

COPY generate_rules.py .
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "generate_rules.py"]