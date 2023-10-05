from django.db import models
from django.urls import reverse


class Shop(models.Model):
    MODEL = (
        ('B650WB-1B', 'B650WB-1B'),
        ('MTP-VD03B-1A', 'MTP-VD03B-1A'),
        ('MTP-1308D-1A', 'MTP-1308D-1A'),
        ('MTP-VD01G-1B', 'MTP-VD01G-1B')
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

class Comment(models.Model):
     STARS = (
         ('Оценка: 1', 'Оценка: 1'),
         ('Оценка: 2', 'Оценка: 2'),
         ('Оценка: 3', 'Оценка: 3'),
         ('Оценка: 4', 'Оценка: 4'),
         ('Оценка: 5', 'Оценка: 5')
     )
     review_object = models.CharField('Укажите название часов:', max_length=100)
     review_created_at = models.DateTimeField(auto_now_add=True)
     review_text = models.TextField('Отзыв:', blank=True, null=True)
     review_start = models.CharField('Укажите свою оценку:', max_length=100, choices=STARS)

     def __str__(self):
         return self.review_start

     class Meta:
         verbose_name = 'Отзывы'
         verbose_name_plural = 'Отзывы'