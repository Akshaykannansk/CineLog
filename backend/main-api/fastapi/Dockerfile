FROM python:3.12-slim

COPY fastapi_requirements.txt .
RUN pip install -r fastapi_requirements.txt
WORKDIR /app

COPY . /app



EXPOSE 80

CMD ["uvicorn", "app.main:app","--reload", "--host", "0.0.0.0", "--port", "80"]