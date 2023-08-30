from .models import *

menu_titles = {
    '': 'Главное меню',
    'publications': 'Публикации',
    'make_publication': 'Опубликовать',
}

class DataMixin:
	"""Базовый миксин для классовых представлений"""

	def get_menu_context(self,is_authenticated: bool, selected_title = 'none'):
		context = {}
		context['selected_title'] = selected_title
		context['menu_titles'] = menu_titles.copy()

		if is_authenticated:
			context['menu_titles']['profile'] = 'профиль'
		else:
			context['menu_titles']['registration'] = 'регистрация'
			context['menu_titles']['authentication'] = 'войти'

		if 'selected_title' not in context:
			context['selected_title'] = 'none'

		return context