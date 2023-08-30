from django.contrib import admin

from .models import *

# class AddCarPhotos(admin.TabularInline):
#     model = CarPhoto
#     extra = 1


# class AddModulePhoto(admin.TabularInline):
#     model = ModulePhoto
#     extra = 1


class CarAdmin(admin.ModelAdmin):
    """Класс для переработки интерфейса добавления автомобиля"""

    # inlines = [AddCarPhotos]
    list_display = ('brand', 'model')
    search_fields = ('brand__brand', 'model__model')

# class ModuleAdmin(admin.ModelAdmin):
#     """Класс для переработки интерфейса добавления модуля"""

#     inlines = [AddModulePhoto]

admin.site.register(ModuleType)
admin.site.register(Module)
admin.site.register(Car, CarAdmin)
admin.site.register(CarBrand)
admin.site.register(CarModel)
