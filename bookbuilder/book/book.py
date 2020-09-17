from .models import Book


def add_book(title, author):
    return Book.objects.create(author=author, title=title)


def list_books():
    return Book.objects.all()


def get_book(title):
    return Book.objects.get(title=title)


def delete_book(title):
    Book.objects.get(title=title).delete()

