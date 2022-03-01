FROM node:current-alpine

WORKDIR /app
COPY . /app

ENV VITE_IMAGE_API=""
RUN npm run build

FROM nginx:alpine

COPY --from=0 /app/build /usr/share/nginx/html

WORKDIR /usr/share/nginx/html

# /data/data.json should be a shared volume where ingresses get downloaded to
RUN mkdir -p /data && mv data.json /data/data.json && ln -s /data/data.json data.json
