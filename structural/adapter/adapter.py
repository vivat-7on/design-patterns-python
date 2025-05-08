class OldPrinter:
    def do_print(self, text):
        print(f"[OldPrinter] {text}")


class Printer:
    def print_next(self, text):
        raise NotImplementedError


class PrinterAdapter(Printer):
    def __init__(self, adaptee: OldPrinter):
        self.adaptee = adaptee

    def print_next(self, text):
        self.adaptee.do_print(text)


old_printer = OldPrinter()
printer = PrinterAdapter(old_printer)

printer.print_next("Hello world!")

# =================

class LegacyWeatherService:
    def get_weather_data(self):
        return "sunny"

class WeatherProvider:
    def fetch_weather(self):
        ...

class WeatherProviderAdapter(WeatherProvider):
    def __init__(self, adaptee: LegacyWeatherService):
        self.adaptee = adaptee

    def fetch_weather(self):
        return self.adaptee.get_weather_data()
