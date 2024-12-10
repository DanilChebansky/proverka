import requests
from main import GetHandler, server_ip1, server_port1
from http.server import HTTPServer


server = HTTPServer((server_ip1, server_port1), GetHandler)

url = f'http://{server_ip1}:{server_port1}'

response = requests.get(url)
answer = str(response._content)[2:].split('\\n')
for i in range(len(answer)-1):
    print(answer[i])
