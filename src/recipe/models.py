from django.db import models

# Create your models here.
from django.utils.text import slugify

def rate_choices():
    return [
        ("⭐", "⭐"),
        ("⭐⭐", "⭐⭐"),
        ("⭐⭐⭐", "⭐⭐⭐"),
        ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
        ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐")
    ]


class Category(models.Model):
    content = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slag = slugify(self.content)
    
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.content


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    prep = models.IntegerField()
    cook = models.IntegerField()
    yields = models.IntegerField()
    step = models.TextField()
    img = models.ImageField()
    rate = models.CharField(max_length=256, choices=rate_choices())
    data = models.DateField(auto_now_add=True)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    subject = models.CharField(max_length=512)
    message = models.TextField()

    def __str__(self):
        return self.name
