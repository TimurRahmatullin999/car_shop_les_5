from django.db import models

# Create your models here.

class Buyer(models.Model):
    id_buyer = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Имя', max_length=50)
    surname = models.CharField(verbose_name='Фамилия', max_length=100)
    patronymic = models.CharField(verbose_name='Отчество', max_length=100,null=True, blank=True)
    birthday = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(verbose_name='e-mail')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.surname}'

class Owner(models.Model):
    id_owner = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Имя', max_length=50)
    surname = models.CharField(verbose_name='Фамилия', max_length=100)
    patronymic = models.CharField(verbose_name='Отчество', max_length=100,null=True, blank=True)
    birthday = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
        ordering = ['name']


class Storage(models.Model):
    id_storage = models.AutoField(primary_key=True)
    street = models.CharField(verbose_name='Улица', max_length=250)
    number_of_street = models.PositiveIntegerField(verbose_name='Номер дома')

    def __str__(self):
        return f'{self.street} {self.number_of_street}'

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'
        ordering = ['street']

class Car(models.Model):
    id_car = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='Название', max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', blank=True)
    mileage = models.PositiveIntegerField(verbose_name='Пробег')
    id_owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE
    )
    id_storage = models.ForeignKey(
        Storage,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ['title']


class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    offered_price = models.PositiveIntegerField(verbose_name='Предполагаемая цена')
    meeting_date = models.DateField(verbose_name='Дата встречи')
    id_buyer = models.ForeignKey(
        Buyer,
        on_delete=models.CASCADE
    )
    id_car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['id_order']

    def __str__(self):
        return f"{self.meeting_date}, покупатель: {self.id_buyer}, машина:{self.id_car}"


class HistoryOrder(models.Model):
    id_order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE
    )
    date_make_order = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Дата заказа'
        verbose_name_plural = 'Даты заказов'
        ordering = ['date_make_order']