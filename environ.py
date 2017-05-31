from urllib.parse import parse_qs
import sys
from wsgiref.simple_server import make_server

ehtml = """
    <html>
    <body>
    
    </body>
    </html>
"""

def web_application(environ, start_response):
    print("Http events!")

    response_body = ""
    for key, val in sorted(environ.items()):
        response_body += ("%s: %s\n" % (key, val))
    '''
    response_body = [
        "%s: %s" % (key, val) for key, val in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)
    '''
    start_response("200 OK", [('Content-Type','text/plain; charset=utf-8')])
    return [response_body.encode()]

if __name__ == '__main__':
    print("Start program")
    httpd = make_server('127.0.0.1', 8000, web_application)
    httpd.handle_request()
    httpd.server_close()

