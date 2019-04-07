from django.db import models

# Create your models here.
from django.db import models
from django import forms

class CharityProject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    submitter = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    submission_date = models.DateTimeField()
    stakeholder = models.ManyToManyField('CharityStakeholder', blank=True)
    ledger = models.OneToOneField('CharityLedger', blank=True, on_delete='cascade')
    bannerimage = models.ImageField(default='default.jpg', upload_to='project_pics')

    def __str__(self):
        return self.name


class CharityStakeholder(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CharityLedger(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(default=0, max_digits=11, decimal_places=2)

    def get_balance(self):
        ledger_entries = LedgerEntry.objects.filter(ledger=self.pk)
        balance = sum(i.entryamount for i in ledger_entries)
        self.balance = balance
        self.save()
        return balance

    get_balance.short_description = 'Balance'

    def __str__(self):
        return self.name


class CharityGoal(models.Model):
    name = models.CharField(max_length=50)
    parentgoal = models.OneToOneField('CharityGoal', null=True, blank=True, on_delete='cascade')
    goalamount = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    pledgedamount = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    distributed = models.BooleanField(default=False)

    def get_needed(self):
        return self.goalamount - self.pledgedamount

    get_needed.short_description = 'Needed'

    def __str__(self):
        return self.name


class LedgerEntry(models.Model):
    entrycomment = models.CharField(max_length=150, blank=True)
    entryamount = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    datetime = models.DateTimeField()
    ledger = models.ForeignKey(CharityLedger, on_delete=models.CASCADE)
    goal = models.ForeignKey(CharityGoal, on_delete=models.CASCADE)

    def __str__(self):
        return self.entrycomment
