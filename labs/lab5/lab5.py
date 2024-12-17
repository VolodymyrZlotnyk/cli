class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}, {self.genre})"


class HomeLibrary:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Книга '{book.title}' додана до бібліотеки.")
        else:
            print("Об'єкт не є книгою!")

    def remove_book(self, index):
        if 0 <= index < len(self.books):
            removed_book = self.books.pop(index)
            print(f"Книга '{removed_book.title}' видалена з бібліотеки.")
        else:
            print("Неправильний індекс!")

    def find_books(self, author=None, year=None, genre=None):
        results = self.books
        if author:
            results = [book for book in results if book.author.lower() == author.lower()]
        if year:
            results = [book for book in results if book.year == year]
        if genre:
            results = [book for book in results if book.genre.lower() == genre.lower()]
        return results

    def get_book_by_index(self, index):
        if 0 <= index < len(self.books):
            return self.books[index]
        else:
            print("Неправильний індекс!")
            return None

    def display_books(self):
        if self.books:
            for idx, book in enumerate(self.books):
                print(f"{idx}: {book}")
        else:
            print("Бібліотека порожня.")


library = HomeLibrary()

library.add_book(Book("1984", "George Orwell", 1949, "Dystopian"))
library.add_book(Book("Brave New World", "Aldous Huxley", 1932, "Science Fiction"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"))

print("\nУсі книги в бібліотеці:")
library.display_books()

print("\nПошук книг за автором 'George Orwell':")
found_books = library.find_books(author="George Orwell")
for book in found_books:
    print(book)

print("\nВидалення книги за індексом 1:")
library.remove_book(1)

print("\nОновлений список книг:")
library.display_books()

print("\nОтримання книги за індексом 0:")
book = library.get_book_by_index(0)
if book:
    print(book)