# custom_tags.py

from django import template
import random

register = template.Library()

@register.filter(name='shuffle')
def shuffle_queryset(queryset):
    """
    Shuffles the given queryset.
    """
    if queryset:
        return random.sample(list(queryset), len(queryset))
    else:
        return queryset
