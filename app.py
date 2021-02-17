from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

import socket

try: 
    server_name = socket.gethostname() 
    server_ip = socket.gethostbyname(server_name) 
except: 
    server_name = "Unable to get Hostname"
    server_ip = "Unable to get IP"


app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def index():
    return render_template('index.html', server_ip = server_ip, server_name = server_name)
    