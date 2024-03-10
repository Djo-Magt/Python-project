from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()

# Create your models here.
class BlogPost (models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title) 

        super().save(*args, **kwargs)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    wikipedia = models.URLField(blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):

    ADVENTURE = "AV"
    THRILLER = "TR"
    FANTASY = "FS"
    ROMANCE = "RM"
    HORROR = "HR"
    SCIENCE_FICTION = "SF"

    GENRES = [
        (ADVENTURE, "Aventure"),
        (THRILLER, "Thriller"),
        (FANTASY, "Fantastique"),
        (ROMANCE, "Romance"),
        (HORROR, "Horreur"),
        (SCIENCE_FICTION, "Science-fiction"),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)
    summary = models.TextField(blank=True)
    category = models.CharField(max_length=25, blank=True, choices=GENRES)
    stock = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self) -> str:
        return self.title

