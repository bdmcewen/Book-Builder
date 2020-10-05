from .models import Paragraph


def add_paragraph1(chapter, text):
    paragraph = Paragraph.objects.create(chapter=chapter, order=-1, text=text)
    paragraph.order = len(list_paragraphs(chapter))
    paragraph.save()
    return paragraph


def list_paragraphs(chapter):
     return Paragraph.objects.filter(chapter=chapter).order_by('order')


def get_paragraph_num(chapter, order):
    return Paragraph.objects.get(chapter=chapter, order=order)


def set_paragraph_text(chapter, paragraph_num, text):
    c = get_paragraph_num(chapter, paragraph_num)
    c.text = text
    c.save()


def set_paragraph_order(chapter, paragraph_num, order):
    c = get_paragraph_num(chapter, paragraph_num)
    c.order = order
    c.save()


def delete_paragraph(chapter, paragraph_num):
    Paragraph.objects.get(chapter=chapter, order=paragraph_num).delete()

