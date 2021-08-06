from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MinCategory(models.Model):
    name = models.CharField(max_length=255)
    mincat = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="images/")
    stock = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey(MinCategory, on_delete=CASCADE)
    price = models.FloatField()
    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
