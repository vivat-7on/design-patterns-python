class BookCollection:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def __iter__(self):
        return ForwardBookIterator(self.books)

    def reverse_iter(self):
        return ReverseBookIterator(self.books)


class ForwardBookIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        raise StopIteration


class ReverseBookIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        books_len = len(self.books)
        if self.index < books_len:
            book = self.books[books_len - self.index - 1]
            self.index += 1
            return book
        raise StopIteration


collection = BookCollection()
collection.add("1984")
collection.add("Brave New World")
collection.add("The Hobbit")

print("Вперёд:")
for book in collection:
    print(book)

print("Назад:")
for book in collection.reverse_iter():
    print(book)
