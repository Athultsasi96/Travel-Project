from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import about
# Create your views here.
def fun(request):
    obj=place.objects.all()
    return render(request,"index.html",{'results':obj})
def about(request):
    obj1=about.objects.all()
    return render(request,"index.html",{'place':obj1})

