from django.db import models

# Create your models here.
from django.db import models
from django import forms
from django.contrib.auth.models import User


class CharityProject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    submission_date = models.DateTimeField()
    stakeholder = models.ManyToManyField(User, blank=True, related_name='stakeholderuser')
    owner = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name='owneruser')
    bannerimage = models.ImageField(default='default.jpg', upload_to='project_pics')

    def __str__(self):
        return self.name


class CharityStory(models.Model):
    heading = models.CharField(max_length=100)
    submission_date = models.DateTimeField()
    story_text = models.TextField()
    charityproject = models.ForeignKey(CharityProject, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading


class CharityLedger(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    charityproject = models.ForeignKey(CharityProject, on_delete=models.CASCADE)

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
    entrycomment = models.CharField(max_length=150, blank=True, verbose_name="Comment")
    entryamount = models.DecimalField(default=0, max_digits=11, decimal_places=2, verbose_name='Amount')
    datetime = models.DateTimeField()
    ledger = models.ForeignKey(CharityLedger, on_delete=models.CASCADE)
    goal = models.ForeignKey(CharityGoal, on_delete=models.CASCADE)

    def __str__(self):
        return self.entrycomment
