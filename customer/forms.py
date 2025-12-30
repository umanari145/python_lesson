from django import forms
from .models import Customer, Prefecture
from django.core.exceptions import ValidationError
from datetime import date

class CustomerForm(forms.ModelForm):
    """顧客登録フォーム"""
    
    class Meta:
        model = Customer
        fields = ['customer_no', 'name', 'registered_date', 'pref']
        widgets = {
            'customer_no': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '会員番号を入力'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前を入力'
            }),
            'registered_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            # forms.Selectは、ForeignKey(Prefecture)フィールドのため、
            #選択肢（Prefectureのレコード一覧）は自動でセットされます
            'pref': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'customer_no': '会員番号',
            'name': '名前',
            'registered_date': '登録日',
            'pref': '都道府県',
        }
    
    def clean_name(self):
        """名前のバリデーション"""
        name = self.cleaned_data['name']
        
        # 20文字以下のチェック
        if len(name) > 20:
            raise ValidationError('名前は20文字以内で入力してください')
        
        return name
    
    def clean_registered_date(self):
        """登録日のバリデーション"""
        registered_date = self.cleaned_data['registered_date']
        
        # 未来の日付は禁止（過去のみ許可）
        if registered_date > date.today():
            raise ValidationError('登録日に未来の日付は指定できません')
        
        return registered_date
