import requests
from main import server_ip1, server_port1


def content():
    """Функция печатает в консоли содержание страницы. Для работы нужно установить библиотеку requests"""
    url = f'http://{server_ip1}:{server_port1}'
    response = requests.get(url)
    answer = str(response._content)[2:].split('\\n')
    for i in range(len(answer)-1):
        print(answer[i])


content()
