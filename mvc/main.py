

from tornado import ioloop
from tornado import httpserver
from tornado.web import Application
from controllers.product_controller import Index, New, Update, Delete

class RunApp(Application):
    def __init__(self) -> None:
        handlers = [
            ("/", Index),
            ("/product/new", New),
            (r"/product/update/(\d+)/status/(\d+)", Update),
            (r"/product/delete/(\d+)", Delete)
        ]

        settings = dict(
            debug=True,
            template_path=r"C:\vscode\udemy-design-patterns\mvc\views",
            static_path=r"C:\vscode\udemy-design-patterns\mvc\static"
        )

        Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    server = httpserver.HTTPServer(RunApp())
    server.listen(5000)
    ioloop.IOLoop.instance().start()
