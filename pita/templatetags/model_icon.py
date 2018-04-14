from django import template

from .. import models

register = template.Library()

@register.filter(name='model_icon')
def model_icon(value):
    return getattr(models, value).get_icon()
