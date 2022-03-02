# Image Service
This image service will serve `svg` images from the [artwork](https://github.com/cncf/artwork) project.

## API

# GET `/img/<name>`
Name will be searched among all CNCF projects and a matching `svg` file will be served.

# GET `/img`
List all the available `svg` images in `artwork`

