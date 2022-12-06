from django.shortcuts import render,redirect,  HttpResponse
from .models import Student,Book
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')

def index(request):
   return render(request, 'index.html')

def display(request):
    Book1=Book.objects.all()
    # print(Book1)
    return render(request, 'display.html', {'books': Book1})

def home(request):
    if request.method=='POST':
        name=request.POST['name']
        fname=request.POST['fname']

        student=Student(name=name,fname=fname)
        student.save()
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def newindex(request):
    if request.method=='POST':
        imag=request.POST['imag']
        name=request.POST['name']
        capt=request.POST['capt']
        review=request.POST['review']

        book=Book(imag=imag,name=name,capt=capt,review=review)
        book.save()
    return render(request, 'newindex.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        return redirect('login')
        # return HttpResponse("HIIIII")
    return render(request, 'singup.html')

def LoginPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('pass')

        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("Galat hai")

    return render(request, 'login.html')

def logoutf(request):
    logout(request)
    return render(request,'login.html')

