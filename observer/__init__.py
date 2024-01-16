
from rich import print
from observer.observer import DefaultSubscription, EmailSubscription, NewsAgency, Observer_A, Observer_B, SMSSubscription, Topic

def observer_project_1():
    topic = Topic()
    observer_a = Observer_A(topic)
    observer_b = Observer_B(topic)

    topic.notify("Notification message")

def observer_project_2():
    news_agency = NewsAgency()
    SMSSubscription(news_agency)
    EmailSubscription(news_agency)
    DefaultSubscription(news_agency)

    print(f"[bold yellow]Subscribers :: [/bold yellow]{news_agency.show_subscribers()}")

    news_agency.add_news("[bold green] New course on Udemy for Python Developers [/bold green]")
    news_agency.notify()

    print(f"[bold red]Unsubscribed :: [/bold red]{type(news_agency.unsubscribe()).__name__}")
    print(f"[bold yellow]Subscribers :: [/bold yellow]{news_agency.show_subscribers()}")

    news_agency.add_news("[bold green] New course on Udemy for Data Engineers [/bold green]")
    news_agency.notify()
