from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from pygments.lexer import default


class Feature(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class ProductMixin(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.FloatField()
    discount_percentages = models.DecimalField(max_digits=3, decimal_places=0)
    estimated_setup_time_by_user = models.CharField(max_length=50, default="10 minut")
    estimated_setup_time_by_system = models.CharField(max_length=50, default="<1 minuta")
    features = models.ManyToManyField(Feature, null=True)
    active = models.BooleanField(default=False)
    support = models.BooleanField(default=False)
    customizable = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def get_price(self):
        return self.price * (100-float(self.discount_percentages))/100 if self.discount_percentages else self.price


class Product(ProductMixin):
    show_on_landing_page = models.BooleanField(default=False)

    slug = models.SlugField(allow_unicode=True, max_length=200, unique=True, blank=True)


    class Meta:
        ordering = ['price']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.slug])


def create_product_image_path(instance, filename):
    name, ext = filename.split('.')
    file_path = 'products/{product}/photos.{ext}'.format(
        product=instance.product, ext=ext)
    return file_path

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=create_product_image_path)
    alt = models.CharField(max_length=50)


class Package(ProductMixin):
    products = models.ManyToManyField(Product)
    main_rgb_color = models.CharField(max_length=10, default='#FFFFFF')
    secondary_rgb_color = models.CharField(max_length=10, default='#FFFFFF')

    slug = models.SlugField(allow_unicode=True, max_length=200, unique=True, blank=True)

    class Meta:
        ordering = ['price']
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Package, self).save(*args, **kwargs)
