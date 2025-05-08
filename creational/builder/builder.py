class UserProfile:

    def __init__(self):
        self.name = None
        self.age = None
        self.address = None
        self.phone = None

    def __str__(self):
        return f"Profile(name={self.name}, age={self.age}, address={self.address}, phone={self.phone})"


class UserProfileBuilder:
    def __init__(self):
        self.profile = UserProfile()

    def name(self, name):
        self.profile.name = name
        return self

    def age(self, age):
        self.profile.age = age
        return self

    def address(self, address):
        self.profile.address = address
        return self

    def phone(self, phone):
        self.profile.phone = phone
        return self

    def build(self):
        return self.profile


builder = UserProfileBuilder()

profile = builder.name("Valera").age(30).address("Moscow").phone("999").build()
print(profile)


# ========================

class Pizza:
    def __init__(self):
        self.size: str = "medium"
        self.cheese: bool = False
        self.pepperoni: bool = False
        self.bacon: bool = False
        self.mushrooms: bool = False

    def __str__(self):
        ingredients = []

        if self.cheese:
            ingredients.append("cheese")
        if self.pepperoni:
            ingredients.append("pepperoni")
        if self.bacon:
            ingredients.append("bacon")
        if self.mushrooms:
            ingredients.append("mushrooms")

        ingredients_str = ", ".join(
            ingredients) if ingredients else "no toppings"
        return f"Pizza(size={self.size}, toppings=[{ingredients_str}])"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def build(self):
        return self.pizza


builder = PizzaBuilder()
pizza = (builder
         .size("large")
         .add_cheese()
         .add_bacon()
         .build())

print(pizza)
