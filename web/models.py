from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=60)
    created_time =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Account: {}".format(self.name)


class Bill(models.Model):
    title = models.CharField(max_length=60)
    amount = models.IntegerField()
    date = models.DateField()
    account = models.ForeignKey(Account)

    def __str__(self):
        return "Bill: {}".format(self.title)
