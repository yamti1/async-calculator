from sanic import Sanic

from server.routes import add_routes


def main():
    app = Sanic("My App")
    add_routes(app)
    app.run()


if __name__ == '__main__':
    main()
