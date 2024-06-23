FROM alpine:latest

WORKDIR /app

COPY src/chal.c src/flag.txt src/source.txt ./

RUN apk add coreutils socat gcc musl-dev

RUN cc chal.c

EXPOSE 9999

CMD socat -d -d TCP-LISTEN:9999,fork SYSTEM:"stdbuf -i0 -o0 -e0 ./a.out"
