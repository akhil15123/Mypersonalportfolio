# home/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Return the value from dictionary based on the key"""
    return dictionary.get(key)
