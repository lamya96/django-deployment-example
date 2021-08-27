from django import template4

register = template.Library()

def cut(value,arg):
    """
    this cuts all value of"arg" from strng
    """
    return value.replace(arg,'')

register.filter('cut',cut)
