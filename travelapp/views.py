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

def addition(request):
    num1 = int(request.POST["num1"])
    num2 = int(request.POST["num2"])
    num3 = num1 + num2

    return render(request, "result.html",{"add":num3})
