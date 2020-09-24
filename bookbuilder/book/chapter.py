from .models import Chapter


def add_chapter(book, title):
    chapter = Chapter.objects.create(book=book, chapter_num=-1, title=title)
    chapter.chapter_num = len(list_chapters(book))
    chapter.save()
    return chapter


def list_chapters(book=None):
    if book:
        books = Chapter.objects.filter(book=book)
    else:
        books = Chapter.objects.all()
    return books.order_by('chapter_num')


def get_chapter(book, title):
    return Chapter.objects.get(book=book, title=title)


def get_chapter_num(book, chapter_num):
    return Chapter.objects.get(book=book, chapter_num=chapter_num)


def set_chapter_title(book, chapter_num, title):
    c = get_chapter_num(book, chapter_num)
    c.title = title
    c.save()


def set_chapter_order(book, chapter_num, order):
    c = get_chapter_num(book, chapter_num)
    c.chapter_num = order
    c.save()


def delete_chapter(book, chapter_num):
    Chapter.objects.get(book=book, chapter_num=chapter_num).delete()

