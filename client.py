import json
import socket
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
        file_config = jim.load(file, Loader=yaml.Loader)
        config.update(file_config)

host, port = config.get('host'), config.get('port')

try:
    sock = socket.socket()
    sock.connect((host, port))
    print('Client was started')

    data = input("Enter data:")

    sock.send(data.encode())
    print(f'Client send data { data }')

    b_response = sock.recv(config.get('buffersize'))
    print(f'Server send data { b_response.decode() }')

except KeyboardInterrupt:
    print('Client shutdown.')
