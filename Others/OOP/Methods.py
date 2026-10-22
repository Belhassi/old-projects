class Book:
    num_of_books = 0
    
    def __init__(self, Title, Author, num_of_pages, Year):
        self.Title = Title
        self.Author = Author
        self.num_of_pages = num_of_pages
        self.Year = Year

        Book.num_of_books += 1

    def info(self):
        return self.Title, self.Author, self.num_of_pages, self.Year

    @classmethod
    def from_string(cls, book_str):
        Title, Author, num_of_pages, Year = book_str.split('-')
        return cls(Title, Author, num_of_pages, Year)

##    @staticmethod
##    def
    
book1 = Book("Sapiens", "Harary", 230, 2020)
book2 = Book.from_string("Peter Pan-James M. Barrie-100-1920")

print(book1.info(), book2.info())

