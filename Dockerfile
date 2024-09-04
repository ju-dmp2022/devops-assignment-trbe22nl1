FROM python:3.12-slim
COPY source /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "calculator.py" ]

