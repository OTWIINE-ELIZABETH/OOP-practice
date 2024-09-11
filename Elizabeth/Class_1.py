# Class: Book
class Book:
    # Attributes: title, author, year
    def __init__(self, title, author, year):
        # Initialize attributes
        self.title = title
        self.author = author
        self.year = year

    # Method: get_details()
    def get_details(self):
        # Return book details
        return f"{self.title} by {self.author} ({self.year})"