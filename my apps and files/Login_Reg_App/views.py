from django.shortcuts import render, redirect, HttpResponse
from .models import User
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "Login_Reg_App/index.html")


def register(request):
    errors = User.objects.validate_reg(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password_hash=password_hash)
    request.session['user_id'] = new_user.id
    return redirect("/success")


def login(request):
    errors = User.objects.validate_login(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect("/")
    users = User.objects.filter(email=request.POST['email'])
    if len(users) != 1:
        messages.error(request, "Incorrect Login")
        return redirect("/")
    correct_password =  bcrypt.checkpw(request.POST['password'].encode(), users[0].password_hash.encode())
    if not correct_password:
        messages.error(request, "Incorrect Login")
        return redirect("/")
    request.session['user_id'] = users[0].id
    return redirect("/success")


def success(request):
    if not 'user_id' in request.session:
        messages.error(request, "Please log in to access this page")
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "Login_Reg_App/success.html", context)


def logout(request):
    request.session.clear()
    return redirect("/")