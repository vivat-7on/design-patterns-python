from typing import Any


class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount}₽ с кредитной карты")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount}₽ через PayPal")


class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount}₽ в криптовалюте")


class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process(self, amount):
        self.strategy.pay(amount)


processor = PaymentProcessor(CreditCardPayment())
processor.process(1000)

processor.set_strategy(PayPalPayment())
processor.process(2500)

processor.set_strategy(CryptoPayment())
processor.process(999)


# =====================================
class DeliveryStrategy:
    def calculate_delivery(self, distance):
        raise NotImplementedError


class Order:
    def __init__(self, distance, delivery_strategy: DeliveryStrategy):
        self.distance = distance
        self.delivery_strategy = delivery_strategy

    def calculate_delivery(self):
        return self.delivery_strategy.calculate_delivery(self.distance)


class CourierDelivery(DeliveryStrategy):
    def calculate_delivery(self, distance):
        return 300


class PostDelivery(DeliveryStrategy):
    def calculate_delivery(self, distance):
        return distance * 10


class PickupDelivery(DeliveryStrategy):
    def calculate_delivery(self, distance):
        return 0


order = Order(distance=15, delivery_strategy=CourierDelivery())
print(order.calculate_delivery())  # 300

order.delivery_strategy = PostDelivery()
print(order.calculate_delivery())  # 150

order.delivery_strategy = PickupDelivery()
print(order.calculate_delivery())  # 0
