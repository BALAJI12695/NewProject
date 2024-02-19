from django.db import models


class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    weight = models.IntegerField()
    dimension = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
