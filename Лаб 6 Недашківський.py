from collections import namedtuple

class Library(object):
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def  searchBookYear(self, year):
        for book in self.books:
            if book.year == year:
                return book

    def searhBookAuthor(self, author):
        written_by_author = []
        for book in self.books:
            if book.author == author:
                written_by_author.append(book)
        return written_by_author

    def searchUnderPrice(self,price):
        books_under_price = []
        for book in self.books:
            if book.price < price:
                books_under_price.append(book)
        return books_under_price


Book = namedtuple('Book', 'name author year price')

library = Library()
library.addBook(Book('Harry Potter', 'J. K. Rowling', '1997', 30))
library.addBook(Book('Hobbit', 'J. R. R. Tolkien', '1937', 45))
library.addBook(Book('The Witcher', 'Andrzej Sapkowski', '1993', 20))
library.addBook(Book('Factfulness', 'Hans Rosling', '1985', 15))
print(library.searchBookYear('1937'))


