FROM python:3.11.5-slim
RUN mkdir -p /.cache && chmod 777 /.cache
RUN mkdir -p /logs && chmod 777 /logs
RUN apt-get update && apt-get -y install gcc g++
COPY src/requirements.txt /src/requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r src/requirements.txt
COPY src/ /src/
EXPOSE 7777
CMD ["python", "src/app.py"]