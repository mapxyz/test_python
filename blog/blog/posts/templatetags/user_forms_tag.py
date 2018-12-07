from django import template
from ..forms import *
register = template.Library()

# @register.simple_tag
# def top_menu():
#    return 1111


@register.inclusion_tag('login.html')
def loginFormTag():
   return {'loginForm':LoginForm()}

