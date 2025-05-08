from xml.etree.ElementTree import indent


class FileSystemEntity:
    def get_size(self):
        raise NotImplementedError


class File(FileSystemEntity):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


class Folder(FileSystemEntity):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, entity: FileSystemEntity):
        self.children.append(entity)

    def get_size(self):
        return sum(child.get_size() for child in self.children)


file1 = File("file1.txt", 100)
file2 = File("file2.txt", 200)

folder1 = Folder("Documents")
folder1.add(file1)
folder1.add(file2)

file3 = File("image.png", 500)

root = Folder("Root")
root.add(folder1)
root.add(file3)

print(root.get_size())  # 800


# =======================


class MenuComponent:
    def show(self):
        raise NotImplementedError


class MenuItem(MenuComponent):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print("    " * indent + self.name)


class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: MenuComponent):
        self.children.append(component)

    def show(self, indent=0):
        print("    " * indent + self.name)
        for child in self.children:
            child.show(indent + 1)


menu = Menu("Main")

file = Menu("File")
file.add(MenuItem("New"))
file.add(MenuItem("Open"))
file.add(MenuItem("Exit"))

edit = Menu("Edit")
edit.add(MenuItem("Undo"))
edit.add(MenuItem("Redo"))

help_ = Menu("Help")

menu.add(file)
menu.add(edit)
menu.add(help_)

menu.show()
