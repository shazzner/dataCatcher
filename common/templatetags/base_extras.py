from django.apps import apps
from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.inclusion_tag('navbar.html', takes_context=True)
def show_navbar(context):
    #models = apps.get_models()
    path = context['request'].path
    return { 'path': path }
    
@register.simple_tag
def navactive(request, urls):
    if request in ( reverse(url) for url in urls.split() ):
        return "active"
    return ""
