# Base realisation
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()

print(f"s1 is s2: {s1 is s2}")


# By decorator
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Config:
    def __init__(self):
        self.settings = {"debug": True}


c1 = Config()
c2 = Config()

print(c1 is c2)  # True


# By metaclass
class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.message = []

    def log(self, msg):
        self.message.append(msg)
        print(f"[LOG]: {msg}")


class AppConfig(metaclass=SingletonMeta):

    def __init__(self, *args, **kwargs):
        if not hasattr(self, "settings"):
            self.settings = dict(kwargs)

    def get(self, key, default=None):
        return self.settings.get(key, default)


cfg1 = AppConfig(debug=True, db_host="localhost")
cfg2 = AppConfig(debug=False)

print('cfg1 is cfg2', cfg1 is cfg2)  # True
print(cfg2.get("db_host"))  # localhost
print(cfg2.get("debug"))  # True
print(cfg2.get("missing", "default"))  # default
