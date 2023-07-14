from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateForm
from account.models import UserProfile



def register(request):
    if request.method == 'POST':
        newname= request.POST.get('username')
        email= request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2= request.POST.get('password2')
        if not newname:
            messages.error(request, 'Username is required')
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        new_user = User.objects.create_user(newname, email, pass1)
        new_user.save()

        # Store user ID in session
        request.session['user_id'] = new_user.id
        return redirect('books')

    return render(request, 'login.html')


def connect(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pswd=request.POST.get('pass')
        print("Username:", uname)
        print("pass:", pswd)
        user=authenticate(request,username=uname,password=pswd)
        if not uname:
            messages.error(request, 'Username is required')
            return redirect('login')

        user = authenticate(request, username=uname, password=pswd)

        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            return redirect('books')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request,"login.html")

def disconnect(request):
    logout(request)
    request.session.clear()
    return redirect('login')

def my_view(request):
    if request.user.is_authenticated:
        # User is authenticated, perform actions for authenticated users
        user_id = request.user.id
        username = request.user.username
        # Additional code...

@login_required
def infos(request):
    
    user_id = request.session.get('user_id')
    
    # Retrieve user information based on the ID
    utilisateurs = User.objects.get(id=user_id)
    
    context = {
        'utilisateur': utilisateurs
    }
    return render(request, 'account.html', context)

@login_required
def update(request):
    user_id = request.session.get('user_id')
    utilisateur = User.objects.get(id=user_id)
    
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect('infos')
    else:
        form = UpdateForm(instance=utilisateur)

    return render(request, 'update.html', {'form': form})