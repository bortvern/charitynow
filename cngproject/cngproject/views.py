from django.core.mail import send_mail
from django.contrib import messages


def home(request):
    return HttpResponse('<p>Charity Now</p>')
