import yaml
import sys


def create_service_data(service_number):
    service_name = f'jupyter_server_{service_number}'
    port_number = 8900 + service_number
    return {
        service_name: {
            'build': './',
            'ports': [f'{port_number}:8888'],
            'volumes': ['./src:/home/ucla/src:ro', './workspaces/a:/home/ucla/my_workspace'],
            'environment': [f'JUPYTER_TOKEN=${{JUPYTER_PASSWORD}}_{service_number}']
        }
    }

master_server_data = {
    'master': {
        'build': './',
        'ports': ['8888:8888'],
        'volumes': ['./src:/home/ucla/src:ro', './workspaces/a:/home/ucla/my_workspace'],
        'environment': ['JUPYTER_TOKEN=${JUPYTER__MASTER_PASSWORD}']
    }
}

yml_data = {
    'version': '3',
    'services': master_server_data
}

n = int(sys.argv[1])

for service_number in range(1,n+1):
    yml_data['services'].update(create_service_data(service_number))

with open('./docker-compose.yml', 'w') as file:
    documents = yaml.dump(yml_data, file)

print(sys.argv)