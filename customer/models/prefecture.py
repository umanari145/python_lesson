from django.db import models


class Prefecture(models.Model):
    """都道府県マスター"""
    code = models.IntegerField(unique=True, verbose_name='都道府県コード')
    name = models.CharField(max_length=10, verbose_name='都道府県名')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '都道府県'
        verbose_name_plural = '都道府県'
        ordering = ['code']

