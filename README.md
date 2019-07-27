# python-geoip2-serverless

Zappa app for doing geoip lookups.

## Instructions

1. Download GeoLite2-City.mmdb from https://dev.maxmind.com/geoip/geoip2/geolite2/
1. Place it in the root directory
1. Initialise Zappa via `zappa init`
1. Deploy via `zappa deploy`
1. Query through (e.g.) `https://xxxxxxxxxx.execute-api.us-west-2.amazonaws.com/dev/<ip>`
