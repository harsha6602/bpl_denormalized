from django.shortcuts import render,redirect
from .models import TeamsInfo
# Create your views here.
def index(request):
    return render(request,"html files/index.html")


def registration(request):
    return render(request,"html files/registration.html")

def login(request):
    return redirect('/admin')

def scores(request):
    return render(request,"html files/scores.html")

def badminton_reg(request):
    return render(request,"html files/badminton_reg.html")

def team_details(request):
    return render(request,'html files/players_info.html')