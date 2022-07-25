FROM codingforentrepreneurs/python:3.9-webapp-slim

#COPY .env /app/.env
COPY ./app /app
COPY ./requirements.txt /requirements.txt
COPY ./entrypoint.sh /entrypoint.sh
COPY ./pipelines /pipelines


RUN chmod +x entrypoint.sh

RUN python3 -m venv /opt/venv && /opt/venv/bin/python -m pip install -r requirements.txt

RUN /opt/venv/bin/python -m pypyr /app/pipelines/ai-model-download

WORKDIR /app

CMD ["./entrypoint.sh"]
