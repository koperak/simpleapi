# simpleapp

## Purpose
Web app with Flask server backend and CSS Bulma frontend. The business concept for is to have an application:
* web based and good looking - support modern CSS framework 👁 
* displaying host and network information - our business 💑 requirements
* easy to deploy and monitor - container based 📦 with easy metrics

### Explanation
If you are interested in details of this project please visit complimentary [blog post](https://blog.insc.pl/flask-web-app-with-bulma-frontend-run-on-docker-with-prometheus-metrics)

## Setup and run
```
git clone https://github.com/koperak/simpleapp.git && cd simpleapp
docker build . -t simpleapp
docker run -d -p 5000:5000 simpleapp
```

## Test
* `http://127.0.0.1:5000/` main web application page
* `http://127.0.0.1:5000/metrics` default metrics 

## Requirements
* Docker
