class Color:
    def fill(self):
        raise NotImplementedError


class Red(Color):
    def fill(self):
        return "красным"


class Green(Color):
    def fill(self):
        return "зелёным"


class Blue(Color):
    def fill(self):
        return "синим"


class Shape:
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    def draw(self):
        print(f"Рисуем круг {self.color.fill()} цветом")


class Square(Shape):
    def draw(self):
        print(f"Рисуем квадрат {self.color.fill()} цветом")


red = Red()
blue = Blue()

circle = Circle(red)
square = Square(blue)

circle.draw()  # Рисуем круг красным цветом
square.draw()  # Рисуем квадрат синим цветом


# ==================


class Device:
    def turn_on(self):
        raise NotImplementedError

    def turn_off(self):
        raise NotImplementedError

    def set_channel(self, n):
        raise NotImplementedError


class TV(Device):
    def turn_on(self):
        print("Включаем телевизор")

    def turn_off(self):
        print("Выключаем телевизор")

    def set_channel(self, n):
        print(f"Переключаем телевизор на {n}-й канал")


class Radio(Device):
    def turn_on(self):
        print("Включаем радио")

    def turn_off(self):
        print("Выключаем радио")

    def set_channel(self, n):
        print(f"Настраиваем радио на {n} волну")


class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

    def set_channel(self, n):
        self.device.set_channel(n)


remote_tv = RemoteControl(TV())
remote_radio = RemoteControl(Radio())

remote_tv.turn_on()
remote_tv.set_channel(5)

remote_radio.turn_on()
remote_radio.set_channel(101)
