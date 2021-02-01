from flask import Flask, render_template
import socket

server_ip = socket.gethostbyname(socket.gethostname())

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', server_ip = server_ip, server_name = socket.gethostname())
    