# myapp/templatetags/custom_tags.py
from django import template

register = template.Library()

@register.simple_tag
def get_navigation_menu():
    return [
        {'name': 'Home', 'url': '/'},
        {'name': 'Products', 'url': '/products/'},
    ]
