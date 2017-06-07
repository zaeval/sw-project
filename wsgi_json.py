from cgi import parse_qs
from wsgiref.simple_server import make_server
import json

def wsgi_appication(environ,start_response):
    print("wsgi handler")
    response = ""

    #for key, val in sorted(environ.items()):
    #    response += "%s: %s\n" % (key, val)
    #print(response)

    try:
        body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        body_size = 0

    body = environ['wsgi.input'].read(body_size)

    d = parse_qs(body)
    x_list = d.get('x'.encode(), [0])
    y_list = d.get('y'.encode(), [0])

    rx = int(x_list[0])
    ry = int(y_list[0])

    sum = rx + ry
    mul = rx * ry
    print("sum : %d, mul : %d" % (sum, mul))

    response_json = json.dumps({'sum':sum, 'mul':mul})

    start_response("200 OK", [('Content-Type','application/json; charset=utf-8')])
    return [response_json.encode()]

if __name__ == "__main__":
    print("Start Program")
    httpd = make_server("", 8001, wsgi_appication)
    httpd.serve_forever()

