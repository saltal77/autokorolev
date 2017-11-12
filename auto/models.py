#-*- coding: utf-8 -*-

from django.db import models

class Interest(models.Model):
    name = models.CharField(verbose_name='Название', max_length=20, default='Блок Важно знать')
    text = models.TextField(verbose_name='Блок Важно знать Текст')

    class Meta:
        verbose_name = 'Блок Важно Знать'
        verbose_name_plural = 'Блок Важно Знать'

    def __str__(self):
        return '{}'.format(self.name)

class TypeOfWorks(models.Model):
    type = models.CharField(verbose_name='Название', max_length=20, default='Название работы')

    class Meta:
        verbose_name = 'Список Тип работ'
        verbose_name_plural = 'Список Тип работ'

    def __str__(self):
        return '{}'.format(self.type)

class ServiceList(models.Model):
    title = models.ForeignKey(TypeOfWorks, verbose_name='Название', default='Название услуги')
    description = models.CharField(verbose_name='Описание', max_length=200, default='Описание услуги')
    class Meta:
        verbose_name = 'Спектр  Услуг'
        verbose_name_plural = 'Спектр  Услуг'

    def __str__(self):
        return '{} {}'.format(self.title, self.description)

class ServiceListTO(models.Model):
    title = models.ForeignKey(TypeOfWorks, verbose_name='Название', default='Название услуги')
    description = models.CharField(verbose_name='Описание', max_length=200, default='Описание Тех регламента')
    class Meta:
        verbose_name = 'Тех  Регламент'
        verbose_name_plural = 'Тех  Регламент'

    def __str__(self):
        return '{} {}'.format(self.title, self.description)

class ServiceItems(models.Model):
    title = models.ForeignKey(TypeOfWorks, verbose_name='Название', default='Название услуги')
    description = models.CharField(verbose_name='Описание', max_length=200, default='Описание услуги')
    price = models.CharField(verbose_name='Цена', max_length=20, default='0')

    class Meta:
        verbose_name = 'Список  Услуг и Цены'
        verbose_name_plural = 'Список  Услуг и Цены'

    def __str__(self):
        return '{} {}'.format(self.title, self.price)

class Comments(models.Model):
    author = models.CharField(verbose_name='Автор', max_length=30)
    text = models.TextField(verbose_name='Отзыв')
    date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    flag = models.BooleanField(verbose_name='Отобразить на сайте', default=False)

    class Meta:
        verbose_name = 'Отзывы клиентов'
        verbose_name_plural = 'Отзывы клиентов'

    def display(self):
        return self.flag

    def __str__(self):
        return '{} {}'.format(self.author, self.date)

class Adress(models.Model):
    name = models.CharField(verbose_name='Как проехать', max_length=30)
    path = models.TextField(verbose_name='Как добратся в сервис')
    street = models.TextField(verbose_name='Точный адрес', default='Юбилейный')
    coords = models.URLField(verbose_name='Координаты google')

    class Meta:
        verbose_name = 'Координаты сервиса'
        verbose_name_plural = 'Координаты сервиса'

    def __str__(self):
        return '{}'.format(self.name)

class ImageOfWorks(models.Model):
    name = models.ForeignKey(TypeOfWorks, verbose_name='Название работы', null=True)
    text = models.CharField(verbose_name='Описание', max_length=40)
    foto = models.ImageField(verbose_name='Фото', upload_to='works', null=True)
    date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Фото работ'
        verbose_name_plural = 'Фото работ'

    def __str__(self):
        return '{} {}'.format(self.name, self.date)



