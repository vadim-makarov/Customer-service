FROM python
WORKDIR /Customer-service/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s -vvv /Customer-service/Customer-service/tests