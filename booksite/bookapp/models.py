from django.db import models

# Create your models here.

#Creating a Models for Category

class Category(models.Model):
    name = models.CharField("Categories", max_length=60)
    slug = models.SlugField(max_length=50)


    def __str__(self):
        return self.name
    
    
class Books(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=100)
    author = models.CharField(max_length=80)
    genre = models.ManyToManyField(Category, related_name="books")
    image = models.ImageField(upload_to="image")
    summary = models.TextField()
    pdf = models.FileField(upload_to="pdf")
    crime_books = models.BooleanField(default=False)
    Biography_books = models.BooleanField(default=False)
    selfHelp_books = models.BooleanField(default=False)
    programming_books = models.BooleanField(default=False)

    def __str__(self):
        return self.title