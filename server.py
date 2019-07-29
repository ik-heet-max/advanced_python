import yaml
import socket
from argparse import ArgumentParser
import json

parser = ArgumentParser()

parser.add_argument(
        '-c', '--config', type=str, required=False,
        help='Sets config file path'
        )

args = parser.parse_args()

config = {
        'host' : 'localhost',
        'port' : 8000,
        'buffersize' : 1024
        }

if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        config.update(file_config)

host, port = config.get('host'), config.get('port')

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    
    print("Socket run with {}:{}".format(host, port))

    while True:
        client, address = sock.accept()
        print("Client {} detected {}:{}".format(client, address[0], address[1]))

        b_request = client.recv(config.get('buffersize'))
        print('Client has sent message: {}'.format(json.loads(b_request.decode())))

        client.send(b_request)
        client.close()
except KeyboardInterrupt:
    print("server shutdown")
