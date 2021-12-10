FROM node:14-alpine3.14

COPY ./vuengo /frontend

RUN npm install -g http-server

WORKDIR /frontend

RUN npm install

RUN npm rebuild node-sass

RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]