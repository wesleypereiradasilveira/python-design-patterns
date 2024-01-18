

from typing import Self
from db import execute


class Product:
    def __init__(self, name: str, price: float, id: int = None) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.status = 1 # active 1, inactive 0

        # if table doesn't exists, create it
        query = """CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            price REAL, 
            status NUMERIC
        );"""

        execute(query)

    def insert(self) -> None:
        query = f"""
            INSERT INTO products (name, price, status)
            VALUES ('{self.name}', '{float(self.price)}', '{self.status}');
        """

        execute(query)

    def update(self) -> None:
        query = f"""
            UPDATE products
            SET status={int(self.status)}
            WHERE id={int(self.id)};
        """

        execute(query)

    def delete(self) -> None:
        query = f"""
            DELETE FROM products 
            WHERE id={int(self.id)};
        """

        execute(query)

    @staticmethod
    def get_products() -> list:
        query = """SELECT * FROM products;"""

        products = execute(query)
        return products
    
    @staticmethod
    def get_product(id: int) -> Self:
        query = f"""
            SELECT id, name, price 
            FROM products
            WHERE id={int(id)};
        """

        product = execute(query)[0]
        product = Product(
            id=product[0],
            name=product[1],
            price=product[2]
        )
        return product

