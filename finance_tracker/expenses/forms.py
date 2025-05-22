from django import forms
from .models import Expense, Income

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount']
