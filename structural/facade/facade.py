class DVDPlayer:
    def on(self): print("DVD включён")

    def play(self): print("Проигрывание фильма")


class Projector:
    def on(self): print("Проектор включён")

    def wide_screen_mode(self): print("Широкоформатный режим")


class Lights:
    def dim(self): print("Свет приглушён")


class Amplifier:
    def on(self): print("Усилитель включён")

    def set_volume(self, level): print(f"Громкость: {level}")


class HomeTheaterFacade:
    def __init__(self, dvd, projector, lights, amp):
        self.dvd = dvd
        self.projector = projector
        self.lights = lights
        self.amp = amp

    def watch_movie(self):
        print("Готовим кинотеатр...")
        self.projector.on()
        self.projector.wide_screen_mode()
        self.lights.dim()
        self.amp.on()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play()


dvd = DVDPlayer()
projector = Projector()
lights = Lights()
amp = Amplifier()

home_theater = HomeTheaterFacade(dvd, projector, lights, amp)
home_theater.watch_movie()


# =================

class Grinder:
    def grind_beans(self):
        print("Молим зёрна...")


class Heater:
    def heat_water(self):
        print("Нагреваем воду...")


class Brewer:
    def brew(self):
        print("Завариваем кофе...")


class MilkFrother:
    def froth_milk(self):
        print("Вспениваем молоко...")


class CoffeeMachineFacade:
    def __init__(self):
        self.grinder = Grinder()
        self.heater = Heater()
        self.brewer = Brewer()
        self.milk_frother = MilkFrother()

    def make_espresso(self):
        self.grinder.grind_beans()
        self.heater.heat_water()
        self.brewer.brew()

    def make_cappuccino(self):
        self.grinder.grind_beans()
        self.heater.heat_water()
        self.brewer.brew()
        self.milk_frother.froth_milk()


machine = CoffeeMachineFacade()
machine.make_espresso()
machine.make_cappuccino()
