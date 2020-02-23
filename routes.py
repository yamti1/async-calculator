from sanic.response import json


def add(request):
    return json(sum(request.json))


def sub(request):
    a, b = request.json
    return json(a - b)


ROUTES = {
    "add": add,
    "sub": sub,
}


def add_routes(app, routes=None):
    routes = routes or ROUTES

    for uri, handler in routes.items():
        app.add_route(handler, uri)