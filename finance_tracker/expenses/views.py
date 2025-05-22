from django.shortcuts import render, redirect
from .models import Expense, Income
from .forms import ExpenseForm, IncomeForm

def home(request):
    expenses = Expense.objects.all()
    incomes = Income.objects.all()

    total_income = sum(income.amount for income in incomes)
    total_expenses = sum(expense.amount for expense in expenses)
    balance = total_income - total_expenses

    if request.method == 'POST':
        if 'add_income' in request.POST:
            income_form = IncomeForm(request.POST)
            if income_form.is_valid():
                income_form.save()
                return redirect('home')
        elif 'add_expense' in request.POST:
            expense_form = ExpenseForm(request.POST)
            if expense_form.is_valid():
                expense_form.save()
                return redirect('home')
    else:
        income_form = IncomeForm()
        expense_form = ExpenseForm()

    context = {
        'income_form': income_form,
        'expense_form': expense_form,
        'expenses': expenses,
        'incomes': incomes,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
    }

    return render(request, 'expenses/home.html', context)
