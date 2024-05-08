from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    print("Oi")
    return render(request, 'home.html')