from main import server

server.server_activate()

server_ip = server.server_address[0]
server_port = server.server_port
print(f'Starting server at http://{server_ip}:{server_port}')

server.handle_request()

server.server_close()
