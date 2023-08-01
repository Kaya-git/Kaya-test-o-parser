from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название товара')
    link = models.URLField(max_length=1000)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self) -> str:
        return self.name
