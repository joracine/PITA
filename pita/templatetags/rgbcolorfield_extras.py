from django import template

register = template.Library()

@register.filter(name='csshex')
def csshex(value):
    return '#' + hex(int(value))[2:].zfill(6)
