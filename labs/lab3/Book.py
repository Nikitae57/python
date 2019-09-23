class Book:
    def __init__(
        self, name, publication_year, n_pages,
        isbn=None, authors=None, publisher=None, price=None
    ):
        self.price = price
        self.publisher = publisher
        self.isbn = isbn
        self.n_pages = n_pages
        self.publication_year = publication_year
        self.name = name
        if authors is None:
            authors = []
        self.authors = authors
