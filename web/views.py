from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
from django.views.generic import View, UpdateView
from django.utils.decorators import method_decorator

# Create your views here.

from django.contrib.auth.models import User
from .models import Account, Bill
from .forms import AccountForm, BillForm



@method_decorator(login_required, name='dispatch')
class AccountListView(View):
    def get(self, request, *args, **kwargs):
        account_form = AccountForm()
        accounts_list = Account.objects.filter(user=self.request.user)
        context = {
            'accounts_list' : accounts_list,
            'account_form' : account_form,
        }
        return render(request, "web/accounts_list.html", context)
    def post(self, request, *args, **kwargs):
        account_form = AccountForm(request.POST)
        if account_form.is_valid():
            account_name  = account_form.cleaned_data['account_name']
            Account.objects.create(user=self.request.user,name=account_name, created_time = timezone.now())
            return HttpResponseRedirect(reverse('accounts_list'))

@method_decorator(login_required, name='dispatch')
class BillsListView(View):
    def get(self, request, *args, **kwargs):
        bill_form = BillForm()
        accounts_list = Account.objects.filter(user=self.request.user)
        account = Account.objects.get(pk=self.kwargs.get('account_id', None))
        bills = account.bill_set.all()
        context = {
            'accounts_list' : accounts_list,
            'account':account,
            'bills' :bills,
            'bill_form':bill_form,
        }
        return render(request, "web/accounts.html", context)

    def post(self, request, *args, **kwargs):
        bill_form = BillForm(request.POST, request.FILES)
        if bill_form.is_valid():
            bill_title = bill_form.cleaned_data['bill_title']
            bill_amount = bill_form.cleaned_data['bill_amount']
            bill_date =  bill_form.cleaned_data['bill_date']
            bill_image =  bill_form.cleaned_data['bill_image']
            account = Account.objects.get(pk=self.kwargs.get('account_id', None))
            account.bill_set.create( title=bill_title, amount=bill_amount, date=bill_date, image=bill_image)
            return HttpResponseRedirect(reverse('accounts', kwargs={'account_id' : self.kwargs.get('account_id', None)}))



@method_decorator(login_required, name='dispatch')
class EditBillView(UpdateView):
    model = Bill
    fields = ['title', 'amount', 'date', 'image']
    template_name = 'web/edit_bill.html'
    def form_valid(self, form):
        account = Account.objects.get(pk=self.kwargs.get('account_id', None))
        updated_bill = account.bill_set.get(pk=self.kwargs.get('pk', None))
        updated_bill.title = form.cleaned_data['title']
        updated_bill.amount = form.cleaned_data['amount']
        updated_bill.date =  form.cleaned_data['date']
        updated_bill.image =  form.cleaned_data['image']
        updated_bill.save()
        return HttpResponseRedirect(reverse('accounts', kwargs={'account_id' : self.kwargs.get('account_id', None)}))

    def get_success_url(self):
        return reverse('accounts', kwargs= {'account_id' : self.kwargs.get('account_id', None)})
