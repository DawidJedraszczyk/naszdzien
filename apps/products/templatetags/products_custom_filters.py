from django import template

register = template.Library()

@register.filter
def has_product(package, product_name):
    return package.products.filter(name=product_name).exists()
