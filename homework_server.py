from cgi import parse_qs
from wsgiref.simple_server import make_server
import sys

sys.path.append('/home/유저이름/module/')
from count_character_from_string import Ccfs

def application(environ,start_response):
    try:
        body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        body_size = 0

    body = environ['wsgi.input'].read(body_size)

    d = parse_qs(body)
    sentense = d.get('sentense'.encode(), [""])[0]
    character = d.get('character'.encode(), [""])[0]

    response_json = Ccfs(sentense,character).getJson()

    start_response("200 OK", [('Content-Type','application/json; charset=utf-8')])
    return [response_json.encode()]

if __name__ == "__main__":
    print("Start Program")
    httpd = make_server("", 80, application())
    httpd.serve_forever()
