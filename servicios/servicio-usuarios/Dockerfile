FROM node:20-alpine
WORKDIR /app
COPY package*.json .
RUN npm install
COPY src ./src
COPY .env .
EXPOSE 8082
CMD ["node", "src/app.js"]