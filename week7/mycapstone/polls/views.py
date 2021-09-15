from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('Hello, World. You are at the polls index.');

# def home(request):
#     return render(request, 'home.html', {'title':'Polls App'});
