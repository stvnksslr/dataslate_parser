FROM python:3.7

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

COPY ./app /app/app
COPY pyproject.toml poetry.lock /app/

RUN pip install --no-cache-dir --pre poetry
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]