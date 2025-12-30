from django.db import models

class Prefecture(models.Model):
    code = models.IntegerField(unique=True, verbose_name='都道府県コード')
    name = models.CharField(max_length=10, verbose_name='都道府県名')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '都道府県'
        verbose_name_plural = '都道府県'
        ordering = ['code']

class Customer(models.Model):
    customer_no = models.IntegerField()
    name = models.CharField(max_length=20)
    registered_date = models.DateField()
    pref = models.ForeignKey(Prefecture, on_delete=models.PROTECT, verbose_name='都道府県')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['customer_no']