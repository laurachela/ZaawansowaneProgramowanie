from datetime import date
import classes.Library as Lb


class Book:
    library: Lb.Library
    public_date: date
    author_name: str
    author_surname: str
    number_of_pages: int

    def __init__(self, library: Lb.Library, publication_date: date, author_name: str, author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'ABOUT:\nAuthor: {self.author_name} {self.author_surname}\nPublication: {self.publication_date}\nPages: {self.number_of_pages}\nLibrary: {self.library}'
