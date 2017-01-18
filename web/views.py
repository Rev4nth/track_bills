from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse

# Create your views here.

from django.contrib.auth.models import User
from .models import Account, Bill
from .forms import AccountForm, BillForm

@login_required()
def accounts_list(request):
    current_user = request.user
    if request.method == 'POST':
        account_form = AccountForm(request.POST)
        if account_form.is_valid() :
            account_name  = account_form.cleaned_data['account_name']
            current_user.account_set.create(name=account_name, created_time = timezone.now())
            return HttpResponseRedirect("/account/")
    else :
        account_form = AccountForm()
    accounts_list  = current_user.account_set.all()
    template_values = {
        'accounts_list' : accounts_list,
        'account_form' : account_form,
    }
    return render(request, "web/accounts_list.html", template_values)


@login_required()
def accounts(request, account_id):
    current_user = request.user
    accounts_list  = current_user.account_set.all()
    account_each = Account.objects.get(pk=account_id)
    if request.method == 'POST':
        bill_form = BillForm(request.POST, request.FILES)
        if bill_form.is_valid():
            bill_title = bill_form.cleaned_data['bill_title']
            bill_amount = bill_form.cleaned_data['bill_amount']
            bill_date =  bill_form.cleaned_data['bill_date']
            bill_image =  bill_form.cleaned_data['bill_image']
            account_each.bill_set.create(title=bill_title, amount=bill_amount, date=bill_date, image=bill_image)
            return HttpResponseRedirect(reverse('accounts', kwargs={'account_id' : account_id}))
    else:
        bill_form = BillForm()
    bills = account_each.bill_set.all()
    template_values = {
        'accounts_list' : accounts_list,
        'account_each' : account_each,
        'bills' : bills,
        'bill_form': bill_form,
    }
    return render(request, "web/accounts.html", template_values)
