from django.http import HttpResponse
from django.shortcuts import render
def home(request, *args, **kwargs):
    context = "jhay"
    return render(request, "home.html", {"context": context})