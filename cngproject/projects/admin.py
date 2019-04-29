from django.contrib import admin
from django import forms
from .models import CharityProject
from .models import CharityStory
from .models import CharityLedger
from .models import CharityGoal
from .models import LedgerEntry


@admin.register(CharityProject)
class CharityProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'submission_date']


@admin.register(CharityStory)
class CharityStoryAdmin(admin.ModelAdmin):
    list_display = ['heading', 'submission_date']


@admin.register(CharityLedger)
class CharityLedgerAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_balance']


@admin.register(LedgerEntry)
class LedgerEntryAdmin(admin.ModelAdmin):
    list_display = ['entryamount', 'datetime', 'goal']


@admin.register(CharityGoal)
class CharityGoalAdmin(admin.ModelAdmin):
    list_display = ['name', 'goalamount', 'pledgedamount', 'get_needed']