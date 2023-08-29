from django import template
from autorage import utils

register = template.Library()

@register.inclusion_tag('autorage/main_menu_panel.html')
def show_menu_panel(selected_title):
    return{
        'selected_title': selected_title,
        'menu_titles': utils.menu_titles
    }