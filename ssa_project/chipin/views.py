from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='users:login')
def home(request):
    return render(request, "chipin/home.html")