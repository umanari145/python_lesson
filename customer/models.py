from django.db import models

class Customer(models.Model):
    customer_no = models.IntegerField()
    name = models.CharField(max_length=20)
    registered_date = models.DateField()
    pref = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['customer_no']