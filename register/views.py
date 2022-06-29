from django.shortcuts import render, redirect  
from register.forms import RegisterForm  
from register.models import Register 

# Create your views here.
def home(request):
    return render(request, 'base.html')  
def create(request):
    if request.method == "POST":
        register = Register(admin_email = request.POST['email'], password = request.POST['password'], fname = request.POST['fname'], lname = request.POST['lname'] )
        register.save()
        return redirect('/login')
def login(request):
    return render(request, 'login.html')

def show(request):
    if request.method == "POST":
        if Register.Objects.filter(admin_email =request.POST['email'], password = request.POST['password']).exist():
            register = Register.objects.get(email=request.POST['email'], password=request.POST['password'])
            return render(request, 'show.html', {'register': register})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)