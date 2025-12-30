from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from ..models import Customer, Product, Sales


class SalesForm(forms.ModelForm):
    """売上登録フォーム"""
    
    class Meta:
        model = Sales
        fields = ['customer', 'product', 'sale_date', 'quantity']
        widgets = {
            'customer': forms.Select(),
            'product': forms.Select(),
            'sale_date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'quantity': forms.NumberInput(attrs={
                'placeholder': '数量を入力',
                'min': 1
            }),
        }
        labels = {
            'customer': '顧客',
            'product': '商品',
            'sale_date': '売上日',
            'quantity': '数量',
        }
    
    def clean_quantity(self):
        """数量のバリデーション"""
        quantity = self.cleaned_data['quantity']
        
        if quantity < 1:
            raise ValidationError('数量は1以上で入力してください')
        
        return quantity
    
    def clean_sale_date(self):
        """売上日のバリデーション"""
        sale_date = self.cleaned_data['sale_date']
        
        # 未来の日付は禁止
        if sale_date > date.today():
            raise ValidationError('売上日に未来の日付は指定できません')
        
        return sale_date

