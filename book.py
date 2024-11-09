class Book:
    def __init__(self, title, author, year, recommendation):
        self.title = title
        self.author = author
        self.year = year
        self.recommendation = recommendation

    def __str__(self):
        return f"'{self.title}' de {self.author} ({self.year}) - puntuacion: {self.recommendation}"