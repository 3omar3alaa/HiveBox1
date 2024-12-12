FROM python:3.12@sha256:752ce4a954589eb94d32849db7ede17ce120945cb71f6feabab3697550932ff9
WORKDIR /app
COPY . /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]