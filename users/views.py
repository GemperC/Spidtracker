from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        print('post')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("login succeful")
            return redirect('projects')
            # Redirect to a success page.
        else:
            messages.success(request,("Invalid credentials"))
            return redirect('login')    
            # Return an 'invalid login' error message.
    else:
        return render(request, 'login.html', {})

    