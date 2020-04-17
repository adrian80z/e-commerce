from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=254, unique=True,
                            default='')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    graphics = models.CharField(max_length=50, blank=True, null=True)
    processor = models.CharField(max_length=50, blank=True, null=True)
    ram = models.CharField(max_length=50, blank=True, null=True)
    battery_life = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
