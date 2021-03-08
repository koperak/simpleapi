from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
import redis, time
import socket


def get_set_hit_count(set= True):
    retries = 5
    while True:
        try:
            if set:
                return cache.incr('hits')
            else:
                return cache.get('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def get_host_information():
    try: 
        server_name = socket.gethostname() 
        server_ip = socket.gethostbyname(server_name) 
    except: 
        server_name = "Unable to get Hostname"
        server_ip = "Unable to get IP"
    
    return server_ip, server_name


app = Flask(__name__)
metrics = PrometheusMetrics(app)
cache = redis.Redis(host='redis', port=6379)

@app.route("/")
def index():
    server_info = get_host_information()
    count = get_set_hit_count()
    return render_template('index.html', server_ip = server_info[0], server_name = server_info[1], count = count)
    
@app.route("/counter")
def counter():
    return get_set_hit_count(set= False)