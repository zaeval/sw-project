from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

ehtml = """
    <html>
    <body>
    <form method="get">
    <p>
        Name : <input type="text" name="name" value="%(name)s">
    </p>
    <p>
        Age : <input type="text" name="age" value="%(age)s">
    </p>
    <p>
        <input type="submit" value="Submit">
    </p>
    </form>
    <p>
        Name: %(name)s <br>
        Age: %(age)s <br>
    </p>
    </body>
    </html>
"""


def web_application(environ, start_response):
    print("Http events!")
    response_body = ""
    for key, val in sorted(environ.items()):
        response_body += ("%s: %s\n" % (key, val))
    print(response_body)
    d = parse_qs(environ['QUERY_STRING'])
    name = d.get('name', [''])[0]
    age = d.get('age', [''])[0]
    name = escape(name)
    age = escape(age)

    response_body = ehtml % {'name':name or "Empty", 'age':age or "Empty"}

    start_response("200 OK", [('Content-Type', 'text/html; charset=utf-8')])
    return [response_body.encode()]


if __name__ == '__main__':
    print("Start program")
    httpd = make_server('127.0.0.1', 8000, web_application)
    httpd.serve_forever()

