FROM python:3.12-slim
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY calculator.py /
COPY calculator_helper.py /
COPY logger.py /
COPY models.py /
COPY calculator_rest_service.py /
ENTRYPOINT [ "python", "calculator.py" ]

