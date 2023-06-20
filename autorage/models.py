import datetime
from django.db import models


class ModuleType(models.Model):
    """Модель типа модуля"""
    type = models.CharField(max_length=64)

    def __str__(self):
        return self.type


class Module(models.Model):
    """Модель модуля машины"""

    type = models.ForeignKey(ModuleType, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return f"{self.type}: {self.name}"


class User(models.Model):
    """Модель аккаунта пользователя"""

    login = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    photo = models.ImageField(upload_to="users")
    reg_date = models.DateTimeField(auto_now_add=True)


class CarBrand(models.Model):
    brand = models.CharField(max_length=31)

    def __str__(self):
        return self.brand


class CarModel(models.Model):
    model = models.CharField(max_length=31)

    def __str__(self):
        return self.model


class Car(models.Model):
    """Модель статьи об автомобиле"""

    brand = models.ForeignKey(CarBrand, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)  # description
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    modules = models.ManyToManyField(Module)

    # owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f"{self.brand} {self.model}"


class Comment(models.Model):
    """Модель комментария пользователя к статье"""

    # autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=256)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class CarPhoto(models.Model):
    """Модель фотографии автомобиля"""

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="cars/%Y/%m/%d/")


class ModulePhoto(models.Model):
    """Модель фотографии модуля"""

    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="modules/%Y/%m/%d/")
