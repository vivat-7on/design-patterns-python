import copy

from creational.builder.builder import Pizza


class UserProfile:
    def __init__(self, name, age, address, phone, preferences):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.preferences = preferences or {}

    def __str__(self):
        return (f"UserProfile(name={self.name}, age={self.age}, "
                f"address={self.address}, phone={self.phone}, "
                f"preferences={self.preferences})")

    def clone(self):
        return copy.deepcopy(self)


original = UserProfile(
    "Valera",
    30,
    "Moscow",
    "999",
    {"theme": "dark"}
)
clone = original.clone()
clone.name = "Valentin"
clone.preferences["theme"] = "light"

print("Original:", original)
print("Clone   :", clone)


#==============

class PrototypePizza(Pizza):
    def clone(self):
        return copy.deepcopy(self)

original = PrototypePizza()
original.size = "medium"
original.cheese = True
original.pepperoni = True

pizza1 = original.clone()
pizza1.bacon = True

pizza2 = original.clone()
pizza2.size = "large"
pizza2.mushrooms = True

print("Original:", original)
print("Pizza 1:", pizza1)
print("Pizza 2:", pizza2)