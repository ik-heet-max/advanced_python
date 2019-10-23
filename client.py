#!usr/bin/env python

import yaml
import socket
from argparse import ArgumentParser
import json
from datetime import datetime
from server.log import client_log_config


parser = ArgumentParser()
parser.add_argument('-i', '--ip', default='localhost')
parser.add_argument('-p', '--port', type=int, default=8000)
parser.add_argument('-a', '--action', default='echo')

args = parser.parse_args()

host = args.ip
port = args.port

logger = client_log_config.logger

try:
    sock = socket.socket()
    sock.connect((host, port))
    print('client run')
    logger.info('client run')

    msg = {'action': args.action,
            'time': datetime.now().timestamp()
            }
    data = json.dumps(msg)

    sock.send(data.encode())
    print('client sent data')
    logger.info('client sent data')
    b_response = sock.recv(1024)
    print('server sent data{}'.format(b_response.decode()))
    logger.info('server sent data{}'.format(b_response.decode()))

except KeyboardInterrupt:
    print('client shutdown')
    logger.info("client shutdown")


