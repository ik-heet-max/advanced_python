#!usr/bin/env python

import yaml
import socket
from argparse import ArgumentParser
import json

parser = ArgumentParser()
parser.add_argument('-i', '--ip', default='localhost')
parser.add_argument('-p', '--port', type=int, default=8000)
parser.add_argument('--key1', default='dog')
parser.add_argument('--value1', default='Brian Griffin')
parser.add_argument('--key2', default='pig')
parser.add_argument('--value2', default='Peppa Pig')

args = parser.parse_args()

host = args.ip
port = args.port
keys = args.key1, args.key2
values = args.value1, args.value2

try:
    sock = socket.socket()
    sock.connect((host, port))
    print('client run')

    msg = {str(keys[0]):str(values[0]),
            str(keys[1]):str(values[1]),
            }
    data = json.dumps(msg)

    sock.send(data.encode())
    print('client set data')
    b_response = sock.recv(1024)
    print('server sent data{}'.format(b_response.decode()))

except KeyboardInterrupt:
    print("client shutdown")


