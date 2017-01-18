from django import forms
from datetime import date

class AccountForm(forms.Form):
    account_name = forms.CharField(max_length=60)


class BillForm(forms.Form):
    bill_title =  forms.CharField(max_length=60)
    bill_amount = forms.IntegerField()
    bill_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker', 'id': 'bill_date', 'type': 'date'}))
    bill_image = forms.ImageField()
