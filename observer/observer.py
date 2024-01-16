
from rich import print
from abc import ABCMeta, abstractmethod

class Topic:
    def __init__(self) -> None:
        self.__observers = []

    def __repr__(self) -> str:
        return "::Observer::"
    
    def register(self, observer) -> None:
        self.__observers.append(observer)

    def notify(self, *args, **kwargs)  -> None:
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

class Observer_A:
    def __init__(self, topic: Topic) -> None:
        topic.register(self)

    def notify(self, topic, *args)  -> None:
        print(f"The {type(self).__name__} received an {args[0]} from {topic}")

class Observer_B:
    def __init__(self, topic: Topic) -> None:
        topic.register(self)

    def notify(self, topic, *args)  -> None:
        print(f"The {type(self).__name__} received an {args[0]} from {topic}")

class NewsAgency:
    def __init__(self) -> None:
        self.__subscribers: list = []
        self.__last_news: str = ""

    def subscribe(self, subscriber) -> None:
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber = None) -> list:
        if not subscriber:
            return self.__subscribers.pop()
        
        return self.__subscribers.remove(subscriber)
    
    def notify(self) -> None:
        for subscriber in self.__subscribers:
            subscriber.notify()

    def add_news(self, news: str) -> None:
        self.__last_news = news

    def show_news(self) -> str:
        return f"Warning: {self.__last_news}"
    
    def show_subscribers(self) -> list:
        return [type(value).__name__ for value in self.__subscribers]
    
class SubscriptionType(metaclass=ABCMeta):
    @abstractmethod
    def notify(self):
        pass

class SMSSubscription(SubscriptionType):
    def __init__(self, news_agency: NewsAgency) -> None:
        self.news_agency = news_agency
        self.news_agency.subscribe(self)

    def notify(self):
        print(f"{type(self).__name__} {self.news_agency.show_news()}")

class EmailSubscription(SubscriptionType):
    def __init__(self, news_agency: NewsAgency) -> None:
        self.news_agency = news_agency
        self.news_agency.subscribe(self)

    def notify(self):
        print(f"{type(self).__name__} {self.news_agency.show_news()}")

class DefaultSubscription(SubscriptionType):
    def __init__(self, news_agency: NewsAgency) -> None:
        self.news_agency = news_agency
        self.news_agency.subscribe(self)

    def notify(self):
        print(f"{type(self).__name__} {self.news_agency.show_news()}")
