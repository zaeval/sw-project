#!/usr/bin/env python3.5
from cgi import parse_qs
from wsgiref.simple_server import make_server

ehtml = """
    <html>
    <body>
    <form method="post">
    <p>
        x : <input type="text" name="x" value="%(sum)s">
    </p>
    <p>
        y: <input type="text" name="y" value="%(mul)s">
    </p>
    <p>
        <input type="submit" value="Submit">
    </p>
    </form>
    <p>
        sum : %(sum)s <br>
        mul :  %(mul)s <br>
    </p>
    </body>
    </html>
"""
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
    x_list = d.get('x', [''])
    y_list = d.get('y', [''])

    x = int(x_list[0])
    y = int(y_list[0])

    sum = x + y
    mul = x * y
    response_body = ehtml % {"sum":sum, "mul":mul}
    start_response("200 OK", [('Content-Type','text/html; charset=utf-8')])
    return [response_body.encode()]

if __name__ == "__main__":
    print("Start Program")
    httpd = make_server("127.0.0.1", 8022, wsgi_appication)
    httpd.serve_forever()

