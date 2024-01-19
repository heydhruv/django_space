from django.shortcuts import render, redirect
from .models import Blackhole
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def blackhole(request):
    if request.method == 'POST':
        data = request.POST
        item_name = data.get('item_name')
        item_dump = data.get('item_dump')
        item_image = request.FILES.get('item_image')

        Blackhole.objects.create(
            item_name = item_name,
            item_dump = item_dump,
            item_image = item_image,
        )
        return redirect('/black')

    recordset = Blackhole.objects.all()

    if request.GET.get('search'):
        search_item_name = request.GET.get('search')
        recordset = recordset.filter(item_name__icontains = search_item_name)
        if not recordset.exists():
            recordset = Blackhole.objects.all()

    else:
        recordset = Blackhole.objects.all()

    context = {'items': recordset}

    return render(request, 'blackhole.html', context)

@login_required(login_url='/login/')
def black(request):
    return render(request, 'black.html')

def delete_item(request, id):

    record = Blackhole.objects.get(id = id)
    record.delete()
    return redirect('/blackhole/')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'invalid username')
            return redirect('/login/')

        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'invalid password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/blackhole/')

    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            invalid_username = User.objects.filter(username=username).exists()
            invalid_email = User.objects.filter(email=email).exists()
            if invalid_username or invalid_email:
                messages.error(request,'Username or email already exists. Please choose a different email or username.')
                return redirect('/register/')
            else:
                record = User.objects.create(
                    email = email,
                    username = username,
                    password = password
                )
                record.set_password(password)
                record.save()
                return redirect('/login/')
        else:
            messages.error(request, 'password do not match')
    return render(request, 'register.html')

@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect('/login/')