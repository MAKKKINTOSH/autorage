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


class Car(models.Model):
    """Модель статьи об автомобиле"""

    brand = models.CharField(max_length=64)  # Toyota
    model = models.CharField(max_length=64)  # Mark 2
    generation = models.CharField(max_length=64)  # 5 generation 1984-1997, X70
    description = models.TextField()  # description
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return f"{self.brand} {self.model} {self.generation}"


class Comment(models.Model):
    """Модель комментария пользователя к статье"""

    autor = models.CharField(max_length=32)
    text = models.CharField(max_length=256)


class User(models.Model):
    """Модель аккаунта пользователя"""

    login = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    photo = models.ImageField(upload_to="users")
    reg_date = models.DateTimeField()


class CarPhoto(models.Model):
    """Модель фотографии автомобиля"""

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="autorage/media/cars")


class ModulePhoto(models.Model):
    """Модель фотографии модуля"""

    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="autorage/media/modules")
