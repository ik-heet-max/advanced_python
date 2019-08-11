#!usr/bin/env python

import yaml
import socket
from argparse import ArgumentParser
import json
from datetime import datetime

parser = ArgumentParser()
parser.add_argument('-i', '--ip', default='localhost')
parser.add_argument('-p', '--port', type=int, default=8000)
parser.add_argument('-a', '--action', default='echo')

args = parser.parse_args()

host = args.ip
port = args.port

try:
    sock = socket.socket()
    sock.connect((host, port))
    print('client run')

    msg = {'action': args.action,
            'time': datetime.now().timestamp()
            }
    data = json.dumps(msg)

    sock.send(data.encode())
    print('client set data')
    b_response = sock.recv(1024)
    print('server sent data{}'.format(b_response.decode()))

except KeyboardInterrupt:
    print("client shutdown")


