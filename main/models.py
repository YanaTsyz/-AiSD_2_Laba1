from django.db import models


class Task(models.Model):
    title = models.CharField('Название необходимой детали', max_length=50)
    task = models.TextField('Описание поломки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'