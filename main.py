import socket
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hellogg():
	hostname = socket.gethostname()
	host_ip = socket.gethostbyname(hostname)
	msg = 'Hellog\n\n' + 'Hostname: ' + hostname + '\nHost IP: ' + host_ip
	return msg

if __name__ == '__main__':
	app.run(host='0.0.0.0')