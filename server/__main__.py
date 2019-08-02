import json
import yaml
import socket
from argparse import ArgumentParser

from actions import resolve
from protocol import validate_request, make_response


parcer = ArgumentParser()

parcer.add_argument(
    '-c', '--config', type=str, required=False,
    help='Sets config file path'
)

args = parcer.parse_args()

config = {
    'host': 'localhost',
    'port': 8000,
    'buffersize': 1024
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

    print(f'Server started with { host }:{ port }')

    while True:
        client, address = sock.accept()
        print(f'Client was detected { address[0] }:{ address[1] }')

        b_request = client.recv(config.get('buffersize'))

        request = json.loads(b_request.decode())

        if validate_request(request):
            actions_names = request.get('action')
            controller = resolve(actions_names)
            if controller:
                try:
                    print(f'Client sent valid request {request}')
                    response = controller(request)
                except Exception as err:
                    print(f'Internal server error: {err}')
                    response = make_response(request, 500, data='Internal server error')
            else:
                print(f'Controller with action name {actions_names} does not exist')
                response = make_response((request, 404, 'Action not found'))
        else:
            response = make_response(request, 404, 'Wrong request')
            print(f'Client sent invalid request {request}')

        str_response = json.dumps(response)
        client.send(str_response.encode())

        client.close()

except KeyboardInterrupt:
    print('Server shutdown.')
