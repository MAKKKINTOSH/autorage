import datetime

from django import template
from autorage.models import Car

tags_register = template.Library()

@tags_register.inclusion_tag('autorage/main_menu_panel.html')
def show_dateline():
    today = datetime.datetime.now()
    return {""}
