from wsgiref.simple_server import make_server


def wsgi_application(environ, start_response):
    print("wsgi handler")
    response = ""
    for key,val in sorted(environ.items()):
        response += "%s : %s\n" % (key,val)
    print(response)
    start_response("200 OK",[('Content-Type','text/html; charset=utf-8')])
    return [response.encode()]
print("Start Program")
httpd = make_server("0.0.0.0", 8000, wsgi_application)
httpd.handle_request()