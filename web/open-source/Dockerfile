FROM python:3.9-alpine3.13
WORKDIR /app
COPY src .
RUN apk update && \
    apk add --no-cache coreutils && \
    pip install --no-cache-dir Flask
EXPOSE 9999
CMD ["python", "server.py"]