FROM node:current-alpine

WORKDIR /app
COPY . /app

ENV VITE_IMAGE_API="" \
    VITE_CARD_CLASSES="grid_md:grid-cols-4_sm:grid-cols-3_xs:grid-cols-1_gap-4" \
    VITE_IMAGE_HEIGHT=32

RUN npm run build

FROM nginx:alpine

COPY --from=0 /app/build /usr/share/nginx/html
COPY --from=0 /app/etc/nginx /etc/nginx

WORKDIR /usr/share/nginx/html

# /data/data.json should be a shared volume where ingresses get downloaded to
RUN mkdir -p /data && mv data.json /data/data.json && ln -s /data/data.json data.json
