FROM python:3.11.5-slim
RUN mkdir -p /.cache && chmod 777 /.cache
RUN mkdir -p /logs && chmod 777 /logs
RUN apt-get update && apt-get -y install gcc g++
COPY src/requirements.txt /src/requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --nocache-dir -r requirements.txt
COPY src/ /src/
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]