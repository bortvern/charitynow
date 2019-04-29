from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import CharityProject
from .models import CharityLedger
from .models import LedgerEntry
# Create your views here.


def home(request):
    projects = CharityProject.objects.all()
    return render(request, 'home.html', {'projects': projects})


def aboutus(request):
    projects = CharityProject.objects.all()
    return render(request, 'about_us.html', {'projects': projects})


def addfunds(request):
    projects = CharityProject.objects.all()
    return render(request, 'addfunds.html', {'projects': projects})


def donatecancel(request):
    projects = CharityProject.objects.all()
    return render(request, 'donatecancel.html', {'projects': projects})


def donatesuccess(request):
    projects = CharityProject.objects.all()
    return render(request, 'donatesuccess.html', {'projects': projects})


def project_detail(request, id):
    try:
        project = CharityProject.objects.get(id=id)
    except CharityProject.DoesNotExist:
        raise Http404('Project not found')
    return render(request, 'project_detail.html', {'project': project})


def ledger_detail(request, id):
    try:
        ledger = CharityLedger.objects.get(id=id)
    except CharityLedger.DoesNotExist:
        raise Http404('Ledger not found')
    return render(request, 'ledger_detail.html', {'ledger': ledger})

def ledger_entries(request, id):
    try:
        entries = LedgerEntry.objects.filter(ledger=id)
    except LedgerEntry.DoesNotExist:
        raise Http404('Entry does not exist')
    return render(request, 'ledger_entries.html', {'entries': entries})


def cngadmin(request):
    projects = CharityProject.objects.all()
    return render(request, 'cngadmin.html', {'projects': projects})