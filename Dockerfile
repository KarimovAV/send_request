FROM python:3.11-slim

WORKDIR .

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./src ./src

CMD ["python", "-m", "pytest", "-s", "-v", "./src/tests/"]