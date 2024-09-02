from django import template

register = template.Library()

@register.filter
def add(value, arg):
    return int(value) + int(arg)

@register.filter
def minus(value, arg):
    return int(value) - int(arg)