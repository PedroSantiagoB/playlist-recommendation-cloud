FROM python:3.9-slim-bullseye

WORKDIR /app

COPY requirements.txt .
COPY app.py .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=52054"]