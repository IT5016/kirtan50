# Book class
class Book:
    def __init__(self, title, author, publication_year, availability=True):
        """
        Initialize a Book object with title, author, publication year, and availability status.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.availability = availability

    def display_book_details(self):
        """
        Display book details.
        """
        print(f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}, Availability: {self.availability}")


# Patron class
class Patron:
    def __init__(self, name, patron_id):
        """
        Initialize a Patron object with name and ID.
        """
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def manage_borrowed_books(self, book):
        """
        Manage the list of borrowed books.
        """
        if book.availability:
            self.borrowed_books.append(book)
            book.availability = False
            print(f"{self.name} has borrowed {book.title}.")
        else:
            print(f"{book.title} is not available.")


# Library class
class Library:
    def __init__(self):
        """
        Initialize a Library object with lists of books and patrons.
        """
        self.books = []
        self.patrons = []

    def add_book(self, book):
        """
        Add a book to the library.
        """
        self.books.append(book)
        print(f"{book.title} has been added to the library.")

    def register_patron(self, patron):
        """
        Register a new patron.
        """
        self.patrons.append(patron)
        print(f"{patron.name} has been registered.")

    def manage_patron_interactions(self, patron, book):
        """
        Manage interactions with the Patron class.
        """
        if patron in self.patrons:
            patron.manage_borrowed_books(book)
        else:
            print(f"{patron.name} is not a registered patron.")


# Create instances of the Book, Patron, and Library classes
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)
patron1 = Patron("John Doe", "P001")
patron2 = Patron("Jane Doe", "P002")
library = Library()

# Simulate various library operations
library.add_book(book1)
library.add_book(book2)
library.register_patron(patron1)
library.register_patron(patron2)

library.manage_patron_interactions(patron1, book1)
library.manage_patron_interactions(patron2, book2)
library.manage_patron_interactions(patron1, book2) 