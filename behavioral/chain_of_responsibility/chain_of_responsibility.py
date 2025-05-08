class Handler:
    def __init__(self):
        self.next = None

    def set_next(self, handler):
        self.next = handler
        return handler

    def handle(self, request):
        if self.next:
            return self.next.handle(request)
        return None


class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("user"):
            return "Ошибка: нет пользователя"
        print("✅ Пользователь авторизован")
        return super().handle(request)


class DataHandler(Handler):
    def handle(self, request):
        if not request.get("data"):
            return "Ошибка: нет данных"
        print("✅ Товары найдены")
        return super().handle(request)

class PaymentHandler(Handler):
    def handle(self, request):
        if not request.get("paid"):
            return "❌ Ошибка: не оплачено"
        print("✅ Оплата прошла")
        return super().handle(request)

class FinalHandler(Handler):
    def handle(self, request):
        return "Успешно обработано!"


auth = AuthHandler()
data = DataHandler()
final = FinalHandler()
payment = PaymentHandler()

auth.set_next(data).set_next(payment).set_next(final)

request = {"user": "Valera", "data": "some info", "paid": True}
print(auth.handle(request))  # ✅ Успешно
print()
print()
bad_request = {"data": "no user"}
print(auth.handle(bad_request))  # ❌ Ошибка: нет пользователя
print()
print()


# ================

class ProfanityFilterHandler(Handler):
    def handle(self, request):
        bad_words = ["bad", "ugly"]
        for word in request["text"].lower().split():
            if word in bad_words:
                return  "❌ Обнаружен мат"
        print("✅ Нет мата")
        return super().handle(request)

class LengthHandler(Handler):
    def handle(self, request):
        if len(request["text"]) < 10:
            return "❌сообщение слишком короткое"
        print("✅ Длина норм")
        return super().handle(request)


class SpamDetectorHandler(Handler):
    def handle(self, request):
        if "http" in request["text"].lower():
            return "❌ Обнаружен спам (ссылки)"
        print("✅ Не спам")
        return super().handle(request)

class FinalApprovalHandler(Handler):
    def handle(self, request):
        return "🎉 Комментарий опубликован!"

comment = {"text": "I love this product!"}


profanity = ProfanityFilterHandler()
length = LengthHandler()
spam = SpamDetectorHandler()
final = FinalApprovalHandler()


profanity.set_next(length).set_next(spam).set_next(final)

print(profanity.handle(comment))
comment = {"text": "buy now http://spam.com"}
print(profanity.handle(comment))

