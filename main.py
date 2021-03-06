import socket
from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def main():
	hostname = socket.gethostname()
	host_ip = socket.gethostbyname(hostname)
	msg = 'Welcome! ' + 'Hostname: ' + hostname + ' Host IP: ' + host_ip
	return msg

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=os.getenv('PORT'))
