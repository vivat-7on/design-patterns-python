class NewsPublisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} получил новость: {news}")


publisher = NewsPublisher()

alice = Subscriber("Alice")
bob = Subscriber("Bob")

publisher.subscribe(alice)
publisher.subscribe(bob)

publisher.notify("Вышел новый Python 3.12!")

publisher.unsubscribe(alice)

publisher.notify("Новая статья про паттерны!")


# ===================


class WeatherStation:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def set_temperature(self, temperature):
        for subscriber in self.subscribers:
            subscriber.update(temperature)


class PhoneDisplay:

    def update(self, temperature):
        print(f"Телефон: температура {temperature}°")


class EmailAlert:

    def update(self, temperature):
        if 30 < temperature or temperature < 0:
            print(f"Email: отправка предупреждения! Температура {temperature}°")


station = WeatherStation()
phone = PhoneDisplay()

email = EmailAlert()

station.subscribe(phone)
station.subscribe(email)

station.set_temperature(20)
station.set_temperature(-5)
station.set_temperature(35)
