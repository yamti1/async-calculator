import math
from sanic.response import json

from worker_thread import run_in_executor


@run_in_executor()
def add(request):
    return json(sum(request.json))


@run_in_executor()
def sub(request):
    a, b = request.json
    return json(a - b)


@run_in_executor()
def factorial(request):
    return json(math.factorial(request.json))


ROUTES = {
    "add": add,
    "sub": sub,
    "factorial": factorial,
}


def add_routes(app, routes=None):
    routes = routes or ROUTES

    for uri, handler in routes.items():
        app.add_route(handler, uri)
