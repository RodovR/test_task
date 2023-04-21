from django import template
from django.http import HttpResponse

from some_name.models import Menu
from some_name.utils import menu

register = template.Library()


@register.simple_tag()
def draw_menu(name: str):
    new_page_all = Menu.objects.all()
    new_page = new_page_all[len(new_page_all) - 1].name
    return new_page
