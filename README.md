# schweizmobil.ch-API
Unofficial API documentation and python example

I love hiking and cycling in Switzerland. I love [map.schweizmobil.ch](https://map.schweizmobil.ch) because it offers excellent maps and track suggestions for free.

With a paid [Switzerland Mobility Plus](https://schweizmobil.ch/en/switzerlandmobility-plus) subscription (currently 35 CHF per year) hiking, cycling, tracks can be created and managed. This repo contains a postman 2.0 Collection JSON describing the API for managing tracks and a demo in python.

I converted the postman file into OpenAPI using https://github.com/DefCon-007/postman-to-openapi-online. Viewing the result with swagger works more or less (the postman references to the user, password and baseUrl variables are not resolved; baseUrl is https://map.schweizmobil.ch).

Please note that I am not affiliated in any way with schweizmobil.ch foundation and this repo is not an official publication of schweizmobil.ch. I created this repo for my training and because I was unable to find online documentation of this API.
