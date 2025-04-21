from django import template

register = template.Library()

@register.filter
def endswith(value, arg): 
    return str(value).endswith(arg)