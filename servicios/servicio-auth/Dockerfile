FROM node:20-alpine
WORKDIR /app
COPY package*.json .
RUN npm install
COPY src ./src
COPY .env .
ENV TZ=America/Bogota
EXPOSE 8081
CMD ["node", "src/app.js"]