import time
import threading


class ChatRoom:
    def __init__(self):
        self.users = []

    def register(self, user):
        self.users.append(user)

    def send(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message, sender)


class User:
    def __init__(self, name, chatroom: ChatRoom):
        self.name = name
        self.chatroom = chatroom
        chatroom.register(self)

    def send(self, message):
        print(f"{self.name} отправил: {message}")
        self.chatroom.send(message, self)

    def receive(self, message, sender):
        print(f"{self.name} получил от {sender.name}: {message}")


chat = ChatRoom()
alice = User("Alice", chat)
bob = User("Bob", chat)

alice.send("Hello!")
bob.send("Hello, Alice!")


# ========================

class ControlTower:
    def __init__(self):
        self.runway_is_empty = True
        self.queue = []

    def request_landing(self, plane):
        print(f"✈️ {plane} запрашивает посадку")
        if self.runway_is_empty:
            self._land(plane)
        else:
            self.queue.append(("land", plane))
            print("❌ Ожидание: полоса занята")

    def request_takeoff(self, plane):
        print(f"✈️ {plane} запрашивает взлёт")
        if self.runway_is_empty:
            self._takeoff(plane)
        else:
            self.queue.append(("takeoff", plane))
            print("❌ Ожидание: полоса занята")

    def _land(self, plane):
        print(f"✅ Разрешено: {plane} садится")
        self.runway_is_empty = False
        time.sleep(5)
        self.runway_is_empty = True
        self._process_next()

    def _process_next(self):
        if self.queue:
            action, plane = self.queue.pop(0)
            if action == "land":
                self._land(plane)
            elif action == "takeoff":
                self._takeoff(plane)

    def _takeoff(self, plane):
        print(f"✅ Разрешено: {plane} взлетает")
        self.runway_is_empty = False
        time.sleep(5)
        self.runway_is_empty = True
        self._process_next()


class Airplane:
    def __init__(self, plane, control_tower: ControlTower):
        self.plane = plane
        self.control_tower = control_tower

    def takeoff(self):
        self.control_tower.request_takeoff(self.plane)

    def landing(self):
        self.control_tower.request_landing(self.plane)


tower = ControlTower()

boeing = Airplane("Boeing737", tower)
airbus = Airplane("Airbus320", tower)
tu154 = Airplane("Tu-154", tower)
sukhoi = Airplane("Sukhoi", tower)

threading.Thread(target=boeing.landing).start()
threading.Thread(target=airbus.takeoff).start()
threading.Thread(target=tu154.landing).start()
threading.Thread(target=sukhoi.takeoff).start()
