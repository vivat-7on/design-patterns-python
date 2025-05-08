class Button:
    def click(self):
        raise NotImplementedError


class Checkbox:
    def check(self):
        raise NotImplementedError


class WindowsButton(Button):
    def click(self):
        print("Нажата кнопка Windows")


class MacButton(Button):
    def click(self):
        print("Нажата кнопка Mac")


class WindowsCheckbox(Checkbox):
    def check(self):
        print("Windows : чекбокс выбран")


class MacCheckbox(Checkbox):
    def check(self):
        print("Mac: чекбокс выбран")


class UIFactory:
    def create_button(self):
        raise NotImplementedError

    def create_checkbox(self):
        raise NotImplementedError


class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

#==================================


class Engine:
    def start(self):
        raise NotImplementedError

class Transmission:
    def use(self):
        raise NotImplementedError

class ElectricEngine(Engine):
    def start(self):
        print("Quiet")

class DieselEngine(Engine):
    def start(self):
        print("Noise")

class ManualTransmission(Transmission):
    def use(self):
        print("Use your hand")


class AutomaticTransmission(Transmission):
    def use(self):
        print("Esy")


class CarFactory:
    def make_engine(self):
        raise NotImplementedError

    def make_transmission(self):
        raise NotImplementedError

class ElectricCarFactory(CarFactory):
    def make_engine(self):
        return ElectricEngine()

    def make_transmission(self):
        return AutomaticTransmission()



class DieselTruckFactory(CarFactory):
    def make_engine(self):
        return DieselEngine()

    def make_transmission(self):
        return ManualTransmission()

def build_vehicle(factory: CarFactory):
    engine = factory.make_engine()
    transmission = factory.make_transmission()

    engine.play()
    transmission.use()

print("Electric car:")
build_vehicle(ElectricCarFactory())

print("\nDiesel truck:")
build_vehicle(DieselTruckFactory())