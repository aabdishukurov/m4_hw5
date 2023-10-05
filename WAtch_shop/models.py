from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'Администратор'),
    (VIPClient, 'VIP Клиент'),
    (CLIENT, 'Клиент')
)

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, 'М'),
    (FEMALE, 'Ж')
)

class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE,
                                    verbose_name="Выберите тип пользователя")
    phone_number = models.CharField('ваш сотовый:', max_length=13)
    age = models.PositiveIntegerField('Укажите возраст?', default=15)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Ваш пол')


class Shop(models.Model):
    MODEL = (
        ('Rolex', 'Rolex'),
        ('А. Lange & Sohne', 'А. Lange & Sohne'),
        ('Grand Seiko', 'Grand Seiko'),
        ('Konstantin Chaykin', 'Konstantin Chaykin')
    )
    title = models.CharField('Укажите название часов:', max_length=100)
    description = models.TextField('Описание часов:', blank=True, null=True)
    image = models.ImageField('Добавьте фото часов:', upload_to='images/')
    review = models.URLField('Укажите ссылку')
    model = models.CharField('Укажите модель часов:', max_length=100, choices=MODEL)
    cost = models.PositiveIntegerField('Укажите цену часов:')
    director = models.CharField('Укажите авторство:', max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'

