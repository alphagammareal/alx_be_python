# programming_paradigm/library_management.py

class Book:
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out

    def check_out(self):
        if not self._is_checked_out:   # only check out if available
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:  # only return if currently checked out
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []   # private list to store Book objects

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)   # calls Book.__str__()
        else:
            print("No books available right now.")
