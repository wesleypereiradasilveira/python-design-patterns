
from singleton.singleton import Singleton, SanityCheck
from singleton.singleton_monostate import SingletonMonostate
from singleton.metaclass import Geek
from singleton.singleton_metaclass import Logger, Database

def singleton():
    s1 = Singleton()
    print(f"Instance 1: {Singleton.get_instance()}")

    s2 = Singleton()
    print(f"Instance 2: {Singleton.get_instance()}")

def singleton_monostate():
    sm1 = SingletonMonostate()
    print(f"sm1 id: {id(sm1)}")
    print(sm1.__dict__)

    sm2 = SingletonMonostate()
    print(f"sm2 id: {id(sm2)}")
    print(sm2.__dict__)

    sm1.name = "Wesley Silveira"
    print(f"sm1: {sm1.__dict__}")
    print(f"sm2: {sm2.__dict__}")

def singleton_metaclass():
    obj = Geek(42, 23)
    print(obj)

    logger_1 = Logger()
    print(f"Logger 1: {id(logger_1)}")

    logger_2 = Logger()
    print(f"Logger 2: {id(logger_2)}")

def singleton_project_1():
    db1 = Database().connect()
    db2 = Database().connect()

def singleton_project_2():
    sc1 = SanityCheck()
    sc2 = SanityCheck()

    sc1.add_server()
    print("Servers Sanity Check initiated...")

    for server in range(4):
        sc1.server_check(server)

    print("Servers Sanity Check finished")

    sc2.change_server()
    print("Servers Sanity Check initiated...")

    for server in range(4):
        sc2.server_check(server)

    print("Servers Sanity Check finished")
