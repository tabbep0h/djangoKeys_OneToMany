from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class Product(models.Model):
    company = models.ForeignKey("Company",on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'