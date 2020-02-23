from sanic import Sanic
from sanic.response import json, text

app = Sanic("My App")


@app.route("/add")
async def root(request):
    return text(sum(request.json))


if __name__ == '__main__':
    app.run()
