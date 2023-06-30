FROM python:3.9.5

EXPOSE 8000

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /app

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0","--port", "8000", "--reload"]