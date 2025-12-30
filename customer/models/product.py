from django.db import models


class Product(models.Model):
    """商品マスター"""
    product_code = models.CharField(
        max_length=20, 
        unique=True, 
        verbose_name='商品コード'
    )
    name = models.CharField(max_length=100, verbose_name='商品名')
    standard_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='標準価格'
    )
    category = models.CharField(
        max_length=50, 
        verbose_name='カテゴリ',
        blank=True
    )
    description = models.TextField(
        verbose_name='説明',
        blank=True
    )
    
    def __str__(self):
        return f"{self.product_code} - {self.name}"
    
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
        ordering = ['product_code']

