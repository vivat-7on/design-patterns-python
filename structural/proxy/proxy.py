class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_from_dick()

    def load_from_dick(self):
        print(f"Загрузка {self.filename} с диска...")

    def display(self):
        print(f"Показ изображения: {self.filename}")


class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


image = ImageProxy("cat.png")
print("Объект создан, но ещё не загружен")
image.display()  # Загрузка с диска, потом показ
image.display()  # Повторно: без загрузки


# =================

class SecretVault:
    def get_secret(self):
        print("42 is the answer")


class VaultProxy:
    def __init__(self, password):
        self.password = password
        self.secret = None

    def get_secret(self, password):
        if self.secret is None:
            if password == self.password:
                self.secret = SecretVault()
                return self.secret.get_secret()
            else:
                raise PermissionError("Access denied")
        print("Уже пущен →", end='')
        return self.secret.get_secret()


vault = VaultProxy(password="qwerty")


try:
    vault.get_secret("1234")
except PermissionError as e:
    print(" ❌ PermissionError")

vault.get_secret("qwerty")  # ✅ "42 is the answer"
vault.get_secret("anything")  # ✅ Уже пущен → "42 is the answer"
