

from tornado.web import RequestHandler
from models.product_model import Product

class Index(RequestHandler):
    def get(self) -> None:
        products: list = Product.get_products()
        self.render("index.html", products=products)

class New(RequestHandler):
    def get(self) -> None:
        self.render("new.html")

    def post(self) -> None:
        name: str = self.get_argument("name", None)
        price: float = self.get_argument("price", None)
        product = Product(name, price)
        product.insert()
        self.redirect("/")

class Update(RequestHandler):
    def get(self, id: int, status: int) -> None:
        product = Product.get_product(id)
        product.status = status
        product.update()
        self.redirect("/")

class Delete(RequestHandler):
    def get(self, id: int) -> None:
        product = Product.get_product(id)
        product.delete()
        self.redirect("/")
