from django.db import models


# Create your models here.
class Book(models.Model):
    ISBN = models.CharField(max_length = 13,null = False,primary_key = True)
    Title = models.CharField(max_length = 30)
    AuthorID = models.ForeignKey("Author") 
    Publisher = models.CharField(max_length = 40)
    PublishDate = models.DateField()
    Price = models.CharField(max_length = 20)
class Author(models.Model):
    AuthorID = models.CharField(max_length = 30,null = False,primary_key = True)
    Name = models.CharField(max_length = 30)
    Age = models.CharField(max_length = 3)
    Country = models.CharField(max_length = 30)
