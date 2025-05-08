# Interface
class Transport:
    def deliver(self):
        raise NotImplementedError


# Realisations
class Truck(Transport):
    def deliver(self):
        print("Доставка по дороге")


class Ship(Transport):
    def deliver(self):
        print("Доставка по морю")


# Abstract factory
class Logistics:
    def create_transport(self) -> Transport:
        raise NotImplementedError

    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()


# Factories realisations
class RoadLogistic(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeeLogistic(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


# ============================================

# Interface
class DocumentProcessor:
    def process(self):
        raise NotImplementedError


# Realisations
class PdfProcessor(DocumentProcessor):
    def process(self):
        print("Обрабатываем PDF")


class TxtProcessor(DocumentProcessor):
    def process(self):
        print("Обрабатываем TXT")


class CsvProcessor(DocumentProcessor):
    def process(self):
        print("Обрабатываем CSV")


# Factory
class DocumentProcessorFactory:
    def get_process(self, file_type: str) -> DocumentProcessor:
        if file_type == "pdf":
            return PdfProcessor()
        elif file_type == "txt":
            return TxtProcessor()
        elif file_type == "csv":
            return CsvProcessor()
        else:
            raise ValueError("Неподдерживаемый тип файла")


# Interface
class Vehicle:
    def go(self):
        raise NotImplementedError


# Realisations
class Car(Vehicle):
    def go(self):
        print('Едем на машине')


class Bike(Vehicle):
    def go(self):
        print('Едем на велосипеде')


class Bus(Vehicle):
    def go(self):
        print('Едем на автобусе')


# Factory
class VehicleFactory:
    _registry = {}

    @classmethod
    def register(cls, key: str, creator: type[Vehicle]):
        cls._registry[key] = creator

    @classmethod
    def create(cls, key: str) -> Vehicle:
        if key not in cls._registry:
            raise ValueError(f"Неизвестный тип транспорта: {key}")
        return cls._registry[key]()


# decorator for register
def register_vehicle(name):
    def wrapper(cls):
        VehicleFactory.register(name, cls)
        return cls

    return wrapper


@register_vehicle("bus")
class Bus(Vehicle):
    def go(self):
        print("Едем на автобусе")
