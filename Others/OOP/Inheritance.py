class Book:
    books = {}
    
    def __init__(self, Title, Author, num_of_pages, Year):
        self.Title = Title
        self.Author = Author
        self.num_of_pages = num_of_pages
        self.Year = Year

        if Author in Book.books:
            Book.books[Author].append((Title, Year))
        else:
            Book.books.update({Author:[(Title, Year)]})
    
    def info(self):
        return self.Title, self.Author, self.num_of_pages, self.Year

    @classmethod
    def from_string(cls, book_str):
        Title, Author, num_of_pages, Year = book_str.split('-')
        return cls(Title, Author, num_of_pages, Year)

class Novel(Book):
    def __init__(self, Title, Author, num_of_pages, Year, genre):
        super().__init__(Title, Author, num_of_pages, Year)
        self.genre = genre

        
book1 = Book("Sapiens", "Harary", 230, 2020)
book2 = Book.from_string("Peter Pan-Harary-100-1920")
book3 = Book("Les Miserables", "Hugo", 70, 1940)
book4 = Book("1984", "George Orwill", 145, 1970)
Novel = Novel("Peace", "Ahmed", 90, 2000, "Fantasy")

import pprint

pprint.pprint(Book.books)


