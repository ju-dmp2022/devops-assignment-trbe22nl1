FROM python:3.12-slim
COPY BE /app
WORKDIR /app
RUN pip install -r requirements.txt
#Workdir rad 2, COPY BE .
ENTRYPOINT [ "python", "calculator.py" ]

