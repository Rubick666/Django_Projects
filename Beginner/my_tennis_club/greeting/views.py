from .models import Members
from django.contrib import messages
from .forms import MembersForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.

def members(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))

def datails(reuqest, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context, reuqest))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    context = {}
    context['form'] = MembersForm()
    return render(request, "template.html", context)

# this is a comment to remember you are doing just great !!

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')
    
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        
        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully :)")
        return redirect('/login/')
    
    return render(request, 'register.html')