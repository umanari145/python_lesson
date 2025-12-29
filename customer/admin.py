from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_no', 'name', 'registered_date', 'pref']
    list_filter = ['customer_no']
    search_fields = ['customer_no', 'title']