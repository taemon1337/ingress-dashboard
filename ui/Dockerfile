FROM node:current-alpine

WORKDIR /app
COPY . /app

RUN npm run build

FROM nginx:alpine

COPY --from=0 /app/build /usr/share/nginx/html

WORKDIR /usr/share/nginx/html

VOLUME /data

# /data/data.json should be a shared volume where ingresses get downloaded to
RUN ln -s /data/data.json data.json
