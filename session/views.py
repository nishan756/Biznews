from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate

from django.contrib import messages

from .forms import UserSignUpForm


def user_login(request):

    if request.user.is_authenticated:

        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("username" , None)

        password = request.POST.get("password" , None)

        if not username or not password:

            messages.warning(request, "You must provide username and password")

        user = authenticate(request, username = username, password = password)

        if user is not None:

            login(request, user)

            messages.success(request, "Login successfull")

            return redirect("home")

        messages.info(request, "Invalid username or password")

    return render(request, "login.html")


def user_logout(request):

    if request.user.is_authenticated:

        logout(request)

    return redirect('login')


def user_signup(request):

    if request.user.is_authenticated:

        return redirect("home")

    form = UserSignUpForm()

    if request.method == "POST":

        form = UserSignUpForm(data = request.POST, files = request.FILES)

        if form.is_valid():

            password = form.cleaned_data.get('password')

            user = form.save(commit = False)

            user.set_password(password)

            user.save()

            messages.success(request, "Successfully created your account. We sent a secure URL to activate your account")

            return redirect("home")
        else:

            messages.warning(request, form.errors)

    return render(request, "signup.html" , {"form" : form})