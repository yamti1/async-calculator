from sanic import Sanic
from sanic.response import json, text

app = Sanic("My App")


@app.route("/")
async def root(_request):
    return text("Hello World!")


if __name__ == '__main__':
    app.run()
