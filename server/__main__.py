import yaml
import socket
from argparse import ArgumentParser
import json
from protocol import validate_request, make_response

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
        request = json.loads(b_request.decode())
        if validate_request(request):
            print('client has sent data {}'.format(rqueste))
            response = make_response(request, 200, data=request.get('data'))
        else:
            print('Client has sent an invalid request {}'.format(request))
            response = make_response(request, 404, 'Wrong request')
        str_response = json.dumps(response)
        client.send(str_response.encode())


        client.close()
except KeyboardInterrupt:
    print("server shutdown")
