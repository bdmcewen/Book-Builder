from .models import Book


def add_book(title, author):
    return Book.objects.create(author=author, title=title)


def list_books(author=None):
    if author:
        return Book.objects.filter(author=author)
    else:
        return Book.objects.all()


def get_book(title):
    return Book.objects.get(title=title)


def get_book_id(pk):
    return Book.objects.get(pk=pk)


def delete_book(title):
    Book.objects.get(title=title).delete()

