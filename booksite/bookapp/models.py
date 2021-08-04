from django.db import models

# Create your models here.

#Creating a Models for Category

class Category(models.Model):
    name = models.CharField("Categories", max_length=60)
    slug = models.SlugField(max_length=20,  blank=True, null=True)


    def __str__(self):
        return self.name
    
    
class Books(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    genre = models.CharField(max_length=80)
    description = models.TextField()
    