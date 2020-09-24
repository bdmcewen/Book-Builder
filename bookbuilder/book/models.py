'''

Data Model Classes

* Reader
    * user*
* Author
    * user*
    * name
* Book
    * author*
    * title
* Chapter
    * book*
    * title
    * chapter_num
* Paragraph
    * chapter*
    * text
    * order
* Image
    * chapter*
    * src
    * alt
    * order

'''

from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk}. {self.name} {self.user.email}'


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk}. {self.title} by {self.author.name}'

    
class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    chapter_num = models.IntegerField()

    def __str__(self):
        return f'{self.pk}. {self.title}'

    
class Paragraph(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    text = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return f'{self.pk}. {self.text[:20]}'

    
class Image(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    src = models.CharField(max_length=100)
    alt = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return f'{self.pk}. {self.src}'
