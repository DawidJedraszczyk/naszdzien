from django.db import models



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, related_name='price', on_delete=models.CASCADE)
    per_person = models.FloatField()
    maximum = models.FloatField()
    discount_price = models.FloatField()
    discount_percent = models.DecimalField(max_digits=3, decimal_places=0)
