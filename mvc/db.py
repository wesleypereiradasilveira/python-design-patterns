
from rich import print as rprint
from sqlite3 import Connection, Cursor
import sqlite3

def execute(query) -> list:
    db_path: str = "./geek.university"
    connection: Connection = sqlite3.connect(db_path)
    cursor: Cursor = connection.cursor()
    result: list = None

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
    except Exception as ex:
        rprint(f"Query execution error: {ex}")
    finally:
        connection.close()
    
    return result
