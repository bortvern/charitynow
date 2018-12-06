from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.conf import settings


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created Please Log In.')
            subject = 'Thank you for joining Charity Now'
            message = 'Welcome to Charity Now. Your account has been created.'
            from_email = settings.EMAIL_HOST_USER
            to_list = [form.cleaned_data['email'], settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, to_list, fail_silently=True)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


