FROM python:3.12@sha256:2fc3687451585d73c06624d54690baf71c61cc2a144549b5b7dbca60048a5fb2
WORKDIR /app
COPY . /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]