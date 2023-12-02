from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='название продукта')
    model = models.CharField(max_length=150, verbose_name='модель продукта')
    release_date = models.DateField(verbose_name='дата выхода на рынок')

    def __str__(self):
        return f'{self.title} - {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Company(models.Model):
    TYPE_CHOICE = (
        ('FC', 'Завод'),
        ('RN', 'Розничная сеть'),
        ('IE', 'Индивидуальный предприниматель'),
    )

    network_type = models.CharField(max_length=2, choices=TYPE_CHOICE, verbose_name='тип звена')
    level = models.PositiveSmallIntegerField(verbose_name='уровень звена', default=0)
    title = models.CharField(max_length=150, verbose_name='название компании')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='страна')
    city = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    house = models.PositiveIntegerField(verbose_name='номер дома')
    products = models.ManyToManyField(Product, related_name='products', verbose_name='продукты')
    provider = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=30, decimal_places=2, verbose_name='задолженность', default=0)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
