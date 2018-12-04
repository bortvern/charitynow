from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import CharityProject
# Create your views here.


def home(request):
    projects = CharityProject.objects.all()
    return render(request, 'home.html', {'projects': projects})


def aboutus(request):
    projects = CharityProject.objects.all()
    return render(request, 'about_us.html', {'projects': projects})


def project_detail(request, id):
    try:
        project = CharityProject.objects.get(id=id)
    except CharityProject.DoesNotExist:
        raise Http404('Project not found')
    return render(request, 'project_detail.html', {'project': project})

