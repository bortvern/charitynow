from django.contrib import admin

from .models import CharityProject
from .models import CharityStakeholder


@admin.register(CharityProject)
class CharityProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'submission_date']


@admin.register(CharityStakeholder)
class CharityStakeholderAdmin(admin.ModelAdmin):
    list_display = ['name']