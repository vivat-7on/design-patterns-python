class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        print(f"Рисуем {self.name} [{self.color}] на позиции ({x}, {y})")


class Tree:
    def __init__(self, x, y, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.draw(self.x, self.y)


class TreeFactory:
    _types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._types:
            cls._types[key] = TreeType(name, color, texture)
        return cls._types[key]


forest = []

for i in range(3):
    type_ = TreeFactory.get_tree_type("Берёза", "зелёный", "гладкая кора")
    forest.append(Tree(i, i * 2, type_))

for tree in forest:
    tree.draw()


# ======================


class Emoji:
    def __init__(self, char, name):
        self.char = char
        self.name = name

    def render(self, x, y):
        print(f"Print {self.char} {self.name} in {x}, {y}")


class EmojiFactory:
    emojis = {}

    @classmethod
    def get_emoji(cls, char, name):
        key = (char, name)
        if key not in cls.emojis:
            cls.emojis[key] = Emoji(char, name)
        return cls.emojis[key]


class EmojiInstance:
    def __init__(self, x, y, emojy: Emoji):
        self.x = x
        self.y = y
        self.emojy = emojy

    def render(self):
        self.emojy.render(self.x, self.y)


factory = EmojiFactory()
instances = [
    EmojiInstance(5, 1, factory.get_emoji("🙂", "smile")),
    EmojiInstance(10, 2, factory.get_emoji("🙂", "smile")),
    EmojiInstance(3, 3, factory.get_emoji("🔥", "fire")),
]

for emoji in instances:
    emoji.render()
