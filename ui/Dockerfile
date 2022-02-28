FROM node:current-alpine

WORKDIR /app
COPY . /app

RUN npm run build

FROM caddy:alpine

WORKDIR /usr/share/caddy
COPY --from=0 /app/build /usr/share/caddy/