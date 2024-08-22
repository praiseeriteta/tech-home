from django.shortcuts import render
from django.http import HttpResponse
from .models import Myblog
# Create your views here.
studentinfo = [
    {
        'id':'1',
        'name': 'mbata',
        'age':'18',
        'course':'python',
    },
    {
        'id':'2',
        'name':'anima',
        'age':'56',
        'course':'html',
    },
    {
        'id':'3',
        'name':'fair',
        'age':'45',
        'course' :'django',
    }

]
def home(request):
    info =studentinfo
    post = Myblog.objects.all()
    return render(request, "work/home.html" ,{'info':info,'post':post})
def about(request):
    return render(request, "work/about.html")
def contact(request):
    return render(request, "work/contact.html")
def blog(request):
    return render(request, "work/blog.html")