FROM alpine:latest
WORKDIR /app
COPY src/picklerick.py .
COPY src/recipe .
RUN apk add coreutils socat python3
EXPOSE 9999
CMD socat -d TCP-LISTEN:9999,fork SYSTEM:"python picklerick.py"