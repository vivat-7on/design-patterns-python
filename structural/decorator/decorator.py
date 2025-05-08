import datetime


class Text:
    def render(self):
        ...


class PlainText(Text):
    def __init__(self, content):
        self.content = content

    def render(self):
        return self.content


class BoldDecorator(Text):
    def __init__(self, wrapped: Text):
        self.wrapped = wrapped

    def render(self):
        return f"<b>{self.wrapped.render()}</b>"


class ItalicDecorator(Text):
    def __init__(self, wrapped: Text):
        self.wrapped = wrapped

    def render(self):
        return f"<i>{self.wrapped.render()}</i>"


text = PlainText("Hello world!")
decorated = ItalicDecorator(BoldDecorator(text))

print(decorated.render())


# =========================
class Sender:
    def send(self):
        ...


class MessageSender(Sender):
    def __init__(self, text):
        self.text = text

    def send(self):
        return self.text


class EncryptedMessageSender(Sender):
    def __init__(self, wrapped: Sender):
        self.wrapped = wrapped

    def send(self):
        return f"{self.wrapped.send()}[ENCRYPTED]"


class TimestampedMessageSender(Sender):
    def __init__(self, wrapped: Sender):
        self.wrapped = wrapped
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def send(self):
        return f"{self.wrapped.send()}\n{self.date}"


text = MessageSender("Letter")
decorated = TimestampedMessageSender(EncryptedMessageSender(text))

print(decorated.send())
