from django import template
import config
from autorage.models import Car

register = template.Library()

@register.inclusion_tag('autorage/main_menu_panel.html')
def show_menu_panel(selected_title):
    return{
        'selected_title': selected_title,
        'menu_titles': config.menu_titles
    }