class Editor:
    def __init__(self):
        self.text = ''

    def type(self, words):
        self.text += words

    def save(self):
        return Memento(self.text)

    def restore(self, memento):
        self.text = memento.get_saved_text()

    def __str__(self):
        return self.text


class Memento:
    def __init__(self, text):
        self._text = text

    def get_saved_text(self):
        return self._text


class History:
    def __init__(self):
        self._history = []

    def save(self, memento):
        self._history.append(memento)

    def undo(self):
        return self._history.pop() if self._history else None


editor = Editor()
history = History()

editor.type("Hello ")
history.save(editor.save())

editor.type("world!")
history.save(editor.save())

print(editor)  # Hello world!

editor.restore(history.undo())  # undo 1
print(editor)  # Hello

editor.restore(history.undo())  # undo 2
print(editor)  # ""


# ============================

class Settings:
    def __init__(self):
        self._theme = None
        self._volume = None
        self._language = None

    def set_theme(self, theme):
        self._theme = theme

    def set_volume(self, volume):
        self._volume = volume

    def set_language(self, language):
        self._language = language

    def save(self):
        return SettingsMemento(self._theme, self._volume, self._language)

    def restore(self, memento):
        self._theme, self._volume, self._language = memento.get_saved_state()

    def __str__(self):
        return f"theme={self._theme}, volume={self._volume}, language={self._language}"


class SettingsMemento:
    def __init__(self, theme, volume, language):
        self._theme = theme
        self._volume = volume
        self._language = language

    def get_saved_state(self):
        return self._theme, self._volume, self._language


class SettingsHistory:
    def __init__(self):
        self._history = []

    def save(self, memento: SettingsMemento):
        self._history.append(memento)

    def undo(self):
        return self._history.pop() if self._history else None


settings = Settings()
history = SettingsHistory()

settings.set_theme("dark")
settings.set_volume(80)
settings.set_language("en")
history.save(settings.save())

settings.set_theme("light")
settings.set_volume(40)
settings.set_language("ru")
history.save(settings.save())

print(settings)  # theme=light, volume=40, language=ru

settings.restore(history.undo())
print(settings)  # theme=dark, volume=80, language=en

settings.restore(history.undo())
print(settings)  # theme=default, volume=default, language=default
