from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import UserManager
from models import User, UserManager, Poke
import bcrypt
import re

def index(request):
    context= {}
    return render(request, 'login_app/index.html', context)
def validate(request):
    context= {}
    registration_errors=User.objects.register_validate(request.POST)
    if len(registration_errors)>0:
        for error in registration_errors:
            messages.error(request, error, context)
        return redirect('/')
    else:
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user=User.objects.create(
        name=request.POST['name'],
        alias=request.POST['alias'],
        email_address=request.POST['email_address'],
        password=password,
        history=0,
        )
        current_user= User.objects.get(email_address=request.POST['email_address'])
        current_user.save()
        request.session['current_user']= User.objects.filter(email_address=request.POST['email_address'])[0].id
        return render(request, 'login_app/index.html',context)
def login(request):
    errors = User.objects.login_validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        print User.objects.filter(email_address=request.POST['email_address'])[0]
        request.session['current_user'] =  User.objects.filter(email_address=request.POST['email_address'])[0].id
        return redirect('/success')

def success(request):
    if "current_user" not in request.session:
        return redirect('/')
    context= {
        "user":User.objects.get(id=request.session['current_user']),
        "other_users":User.objects.all().exclude(id=request.session['current_user']),
        "pokers":User.objects.filter(folks_poked=request.session['current_user']),
        "pokernumber":len(User.objects.filter(folks_poked=request.session['current_user'])),
        "pokecount": len(Poke.objects.filter(receiver=request.session['current_user']))
    }
    return render(request, 'login_app/success.html', context)

def logout(request):
    del request.session['current_user']
    return redirect('/')

def poke(request, id):
    current_user = User.objects.get(id=request.session['current_user'])
    poked = User.objects.get(id=id)
    newpoke=Poke.objects.create(
        creator=current_user,
        receiver=poked
    )
    poked.history+=1
    #poked.pokers.add(current_user)
    current_user.folks_poked.add(poked)
    poked.save()
    #current_user.save()
    print current_user.folks_poked
    #print poked.pokers
    return redirect('/success')