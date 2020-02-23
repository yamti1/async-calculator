from sanic import Sanic
from sanic.response import json, text

app = Sanic("My App")


@app.route("/add")
async def add(request):
    return text(sum(request.json))


@app.route("/sub")
async def sub(request):
    a, b = request.json
    return text(a - b)


if __name__ == '__main__':
    app.run()
