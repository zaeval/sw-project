#!/usr/bin/env python3.5
from cgi import parse_qs
from wsgiref.simple_server import make_server

ehtml = """
    <html>
    <body>
    <form method="post">
    <p>
        Name : <input type="text" name="name" value="%(name)s"> 
    </p>
    <p>
        Age: <input type="text" name="age" value="%(age)s"> 
    </p>
    <p>
        <input type="submit" value="Submit">
    </p>
    </form>
    <p>
        Name : %(name)s <br>
        Age :  %(age)s <br>
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
    name_list = d.get('name', [''])
    age_list = d.get('age', [''])

    rname = name_list[0]
    rage = age_list[0]
    response_body = ehtml % {"name":rname, "age":rage}
    start_response("200 OK", [('Content-Type','text/html; charset=utf-8')])
    return [response_body.encode()]

if __name__ == "__main__":
    print("Start Program")
    httpd = make_server("127.0.0.1", 8022, wsgi_appication)
    httpd.serve_forever()

