from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome to App</h1>')

def hiname(request,name):
    return HttpResponse('<h2>Hello {}</h2>'.format(name))

def add(request,n1,n2):
    x=int(n1)+int(n2)
    return HttpResponse('Sum of {} and {} is {}'.format(n1,n2,x))

def temp(request):
    skill=["Java","Django","Cloud","Database"]
    return render(request,"tmp1.html",context={"skills":skill})

def grt(request,a,b):
    return render(request,"tmp2.html",context={"a":a,"b":b})


def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/aboutus.html')

def base(request):
    return render(request,'base.html')

from django.core.files.storage import FileSystemStorage

def register(request):
    if request.method=="POST":
        title=request.POST.get("title")
        name=request.POST.get("name")
        email=request.POST.get("mail")
        ph=request.POST.get("ph")
        gen=request.POST.get("radio")
        skill=request.POST.getlist("skills")
        if request.FILES:
            ph=request.FILES['photo']
            fs=FileSystemStorage()
            sph=fs.save(ph.name,ph)
            ph_url=fs.url(sph)
        return HttpResponse("Data Received {},{},{},{},{},{},<img src={}>".format(title,name,email,ph,gen,skill,ph_url))
    return render(request,'pages/register.html')