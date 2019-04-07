"""cngproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from projects import views as projects_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', projects_views.home, name='home'),
    url(r'^project/(\d+)/', projects_views.project_detail, name='project_detail'),
    url(r'aboutus/',  projects_views.aboutus, name='aboutus'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('donatecancel', projects_views.donatecancel, name='donatecancel'),
    path('donatesuccess', projects_views.donatesuccess, name='donatesuccess'),
    path('addfunds', projects_views.addfunds, name='addfunds'),
    path('cngadmin/', projects_views.cngadmin, name='cngadmin'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name='users/passwordreset.html'), name='password_reset'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='users/passwordresetconfirm.html'), name='password_reset_confirm'),
    url(r'^password_reset_done/$', auth_views.PasswordResetDoneView.as_view(template_name='users/passwordresetdone.html'), name='password_reset_done'),
    url(r'^password_reset_complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='users/passwordresetcomplete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
