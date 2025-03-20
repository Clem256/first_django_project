from django.db import models


# books db

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title
