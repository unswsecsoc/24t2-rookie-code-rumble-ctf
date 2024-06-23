FROM node:18-alpine

WORKDIR /app

COPY src/package.json ./
COPY src/package-lock.json ./

RUN npm ci

COPY src/ ./

EXPOSE 9999

CMD node index.js
