import json
from socket import *
from argparse import ArgumentParser

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
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    print('Client was started')

    data = input("Enter data:")

    with open('data.json', 'w') as file_json:
        file_json.write(json.dumps(data))

    with open('data.json') as file:
        sock.send(file.read().encode())
        print(f'Client send data {file}')

    b_response = sock.recv(config.get('buffersize'))
    print(f'Server send data {b_response.decode()}')

except KeyboardInterrupt:
    print('Client shutdown.')
