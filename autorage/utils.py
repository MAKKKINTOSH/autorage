from .models import *
from django.contrib.auth.models import User

menu_titles = {
    '': 'Главное меню',
    'publications': 'Публикации',
    'make_publication': 'Опубликовать',
}

class DataMixin:
	"""Базовый миксин для классовых представлений"""

	def get_menu_context(self, user: User, selected_title = 'none'):
		context = {}
		context['selected_title'] = selected_title
		context['menu_titles'] = menu_titles.copy()
		context['is_auth'] = user.is_authenticated
		context['user'] = user

		# if is_authenticated:
		# 	context['menu_titles']['profile'] = 'профиль'
		# else:
		# 	context['menu_titles']['registration'] = 'регистрация'
		# 	context['menu_titles']['authentication'] = 'войти'

		# if 'selected_title' not in context:
		# 	context['selected_title'] = 'none'

		return context