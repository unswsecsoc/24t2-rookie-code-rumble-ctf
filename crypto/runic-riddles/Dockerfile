FROM python:3.9-alpine3.13
WORKDIR /app
COPY src/flag_generator.py .
RUN apk update && \
    apk add --no-cache build-base && \
    apk add --no-cache socat && \
    pip install lz4
EXPOSE 9999
CMD socat -d -d TCP-LISTEN:9999,fork SYSTEM:"python flag_generator.py"