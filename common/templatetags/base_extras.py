from django.apps import apps
from django import template

register = template.Library()

@register.inclusion_tag('navbar.html')
def show_navbar():
    #models = apps.get_models()
    return {}
    
