from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
from http.server import HTTPServer


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)
        print(parsed_path)
        message = '\n'.join([
            'CLIENT VALUES:',
            'client_address=%s (%s)' % (self.client_address,
                                        self.address_string()),
            'command=%s' % self.command,
            'path=%s' % self.path,
            'real path=%s' % parsed_path.path,
            'query=%s' % parsed_path.query,
            'request_version=%s' % self.request_version,
            '',
            'SERVER VALUES:',
            'server_version=%s' % self.server_version,
            'sys_version=%s' % self.sys_version,
            'protocol_version=%s' % self.protocol_version,
            '',
        ])
        self.send_response(200)
        self.end_headers()
        print(message)
        print(self.headers)
        self.wfile.write(message.encode())
        return

    def do_POST(self):
        parsed_path = urlparse(self.path)
        print(parsed_path)
        message = '\n'.join([
            'CLIENT VALUES:',
            'client_address=%s (%s)' % (self.client_address,
                                        self.address_string()),
            'command=%s' % self.command,
            'path=%s' % self.path,
            'real path=%s' % parsed_path.path,
            'query=%s' % parsed_path.query,
            'request_version=%s' % self.request_version,
            '',
            'SERVER VALUES:',
            'server_version=%s' % self.server_version,
            'sys_version=%s' % self.sys_version,
            'protocol_version=%s' % self.protocol_version,
            '',
        ])
        print(message)
        print(self.headers)
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        print(post_body)
        # data = json.loads(post_body)

        reply_body = """<?xml version="1.0" encoding="utf-8"?>
<resource_t xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" obj_id="R1" GUID="c1f4c89a-e34a-4467-83c8-77b4c711b35a" xmlns="http://www.1c-astor.ru/awms/dcd">
    <properties xmlns="http://www.1c-astor.ru/awms/dcd-ws-types">
        <property obj_id="r_FullName" xmlns="">Администратор</property>
        <property obj_id="r_function" xmlns="" />
        <property obj_id="r_Login" xmlns="">1</property>
        <property obj_id="r_Pwd" xmlns="" />
        <property obj_id="r_Available" xmlns="">True</property>
        <property obj_id="r_Blocked" xmlns="">False</property>
        <property obj_id="r_IsDCDAdmin" xmlns="">False</property>
        <property obj_id="r_Scales" xmlns="" />
    </properties>
</resource_t>"""
        self.wfile.write(reply_body.encode('utf-8'))

        return


# if _name_ == '_main_':
server_ip1 = 'localhost'
server_port1 = 8000
server_ip = '192.168.70.101'
server_port = 43217
server = HTTPServer((server_ip1, server_port1), GetHandler)
# print(f'Starting server at http://{server_ip1}:{server_port1}')
# server.serve_forever()
