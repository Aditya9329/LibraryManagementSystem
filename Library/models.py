from django.db import models

# Create your models here.
# book fields
"""1.book_id
2.book_title
3.book_author
4.book_category
5.book_publisher"""
class book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=350)
    book_author = models.CharField(max_length=50)
    book_category = models.CharField(max_length=50)
    book_publisher = models.CharField(max_length=50)

    def __str__(self):
        return self.book_category + " " + self.book_title

# class student(models.Model):
#     pass


# class Librarian(models.Model):
#     pass
