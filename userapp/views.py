from django.shortcuts import render,redirect
from.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm




# Register View
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'New Account Created :' +  user)
            return redirect('login_view')
    context = {"form": form}
    return render(request,'app/register.html',context)



# Login view
def login_view(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is Incorrect' )
            return render(request,'app/login.html')
    context = {}
    return render(request,'app/login.html',context)



# Logout View
def logout_view(request):
    logout(request)
    return redirect('homepage')


# Password Cheng
def chengpwd(request):
    if request.method == "POST":
        pwd=PasswordChangeForm(user=request.user,data=request.POST)
        if pwd.is_valid():
            pwd.save()
            update_session_auth_hash(request,pwd.user)
            return redirect('homepage')
    else:
        pwd=PasswordChangeForm(user=request.user)
    context = {"form": pwd}
    return render(request,'app/chengpwd.html',context)


