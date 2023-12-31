"""
URL configuration for bpl_new project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from bpl_app import views
urlpatterns = [
    path("admin/", admin.site.urls,name="admin"),
    path("",views.index,name="index"),
    path("registration/",views.registration,name="registration"),
    path("login/",views.login,name="login"),
    path("scores/",views.scores,name="scores"),
    path("badminton_reg/",views.badminton_reg,name="badminton_reg"),
    path("player_details/",views.team_details,name="team_details"),
]
