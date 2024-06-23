FROM ubuntu:latest

WORKDIR /app

COPY src/flag.txt src/challenge ./

RUN apt-get update && apt-get install socat -y

EXPOSE 9999

CMD socat -d -d TCP-LISTEN:9999,fork SYSTEM:"stdbuf -i0 -o0 -e0 ./challenge"