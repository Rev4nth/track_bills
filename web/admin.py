from django.contrib import admin

# Register your models here.

from .models import Account, Bill

admin.site.register(Account)
admin.site.register(Bill)
