# from django.http.response import HttpResponse
# from django.shortcuts import redirect, render
# from django.contrib.auth import authenticate, login


# from user.forms import UserForm

# # Create your views here.
# def registration(request):
#     if request.method == 'POST':
#         user = UserForm(request.POST)
#         if user.is_valid():
#             user.save()
#             return redirect("/")
#     else:
#         user = UserForm()
#         return render(request,'registration.html',{'user':user})        

# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect("/")
#     else:
#         # return HttpResponse("Invalid credentials")
#         return render(request,'login.html')
  


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from user.forms import SignUpForm
from django.contrib import messages


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("form gyaaaaaaaaaaaa")
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print("successsssssss")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        print("warishhhhhhhhhhhfffffffffffffffffffh",form)
        if form.is_valid():
            print("warishhhhhhhhhhhh")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                print("login")
                return HttpResponse("login")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    print("nooooo")        
    form = AuthenticationForm()
    return render(request,"login.html",{'login_form':form})
    
