from django.shortcuts import render, HttpResponse, redirect
from ..login_app.models import User

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
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email_address=request.POST['email_address'],
        password=password,
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
    }
    return render(request, 'login_app/success.html', context)

def logout(request):
    del request.session['current_user']
    return redirect('/')
# Create your views here.
