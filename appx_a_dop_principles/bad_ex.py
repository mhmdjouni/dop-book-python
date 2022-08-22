class Author:
    first_name: str
    last_name: str
    nb_books: int

    def __init__(self, first_name, last_name, nb_books):
        self.first_name = first_name
        self.last_name = last_name
        self.nb_books = nb_books

    @property
    def full_name(self) -> str:
        return self.first_name + " " + self.last_name

    def is_prolific(self):
        return self.nb_books > 100
