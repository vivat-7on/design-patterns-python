class ATM:
    def __init__(self):
        self.no_card = NoCard()
        self.has_card = HasCard()
        self.has_pin = HasPin()
        self.state = self.no_card

    def set_state(self, state):
        self.state = state

    def insert_card(self):
        self.state.insert_card(self)

    def eject_card(self):
        self.state.eject_card(self)

    def enter_pin(self):
        self.state.enter_pin(self)

    def withdraw(self):
        self.state.withdraw(self)


class ATMState:
    def insert_card(self, atm): raise NotImplementedError

    def eject_card(self, atm): raise NotImplementedError

    def enter_pin(self, atm): raise NotImplementedError

    def withdraw(self, atm): raise NotImplementedError


class NoCard(ATMState):
    def insert_card(self, atm):
        print("Карта вставлена")
        atm.set_state(atm.has_card)

    def eject_card(self, atm):
        print("Нет карты")

    def enter_pin(self, atm):
        print("Сначала вставьте карту")

    def withdraw(self, atm):
        print("Сначала вставьте карту")


class HasCard(ATMState):
    def insert_card(self, atm):
        print("Карта уже вставлена")

    def eject_card(self, atm):
        print("Карта извлечена")
        atm.set_state(atm.no_card)

    def enter_pin(self, atm):
        print("PIN принят")
        atm.set_state(atm.has_pin)

    def withdraw(self, atm):
        print("Введите PIN сначала")


class HasPin(ATMState):
    def insert_card(self, atm):
        print("Карта уже вставлена")

    def eject_card(self, atm):
        print("Карта извлечена")
        atm.set_state(atm.no_card)

    def enter_pin(self, atm):
        print("PIN уже введён")

    def withdraw(self, atm):
        print("Выдача наличных")
        atm.set_state(atm.no_card)


atm = ATM()

atm.insert_card()  # Карта вставлена
atm.enter_pin()  # PIN принят
atm.withdraw()  # Выдача наличных
atm.eject_card()  # Нет карты (уже извлечена автоматически)

# =====================
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.states = cycle([RedState(), GreenState(), YellowState()])
        self.state = next(self.states)

    def show(self):
        self.state.show()

    def change(self):
        self.state = next(self.states)


class TrafficLightState:
    def show(self): raise NotImplementedError


class RedState(TrafficLightState):
    def show(self):
        print("СТОП")


class GreenState(TrafficLightState):
    def show(self):
        print("ИДИ")


class YellowState(TrafficLightState):
    def show(self):
        print("ЖДИ")


light = TrafficLight()

light.show()  # СТОП
light.change()
light.show()  # ИДИ
light.change()
light.show()  # ЖДИ
light.change()
light.show()  # СТОП
