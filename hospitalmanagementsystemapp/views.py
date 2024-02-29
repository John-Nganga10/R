from django.shortcuts import render, redirect
from hospitalmanagementsystemapp.models import Member, Contact


def index(request):
    if request.method == 'POST':
        messages = Contact(name=request.POST['name'],
                           email=request.POST['email'],
                           subject=request.POST['subject'],
                           message=request.POST['message'])
        messages.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
        members = Member(username=request.POST['username'],
                         email=request.POST['email'],
                         password=request.POST['password'])
        members.save()
        return redirect('/register')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def upload(request):
    return render(request, 'upload.html')


# Create your views here.
def details(request):
    messages = Contact.objects.all()
    return render(request, 'details.html', {'messages': messages})
