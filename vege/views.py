from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import *

# Create your views here.


@login_required(login_url="/login/")
def index(request):
    if request.method == "POST":
        data = request.POST
        file = request.FILES.get("image")
        print(file)
        Recipe.objects.create(
            name=data.get("name"),
            desc=data.get("desc"),
            image=file,
        )
        return redirect("/recipe")

    recipes = Recipe.objects.all()
    context = {"recipes": recipes}

    return render(request, "index.html", context)


def send_email_to_cli(request):
    send_email_to_client()
    redirect("/recipe")


@login_required(login_url="/login/")
def delete(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect("/recipe")


@login_required(login_url="/login/")
def update(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        file = request.FILES.get("image")
        recipe.name = data.get("name")
        recipe.desc = data.get("desc")
        if file:
            recipe.image = file
        recipe.save()
        return redirect("/recipe")

    return render(request, "update.html", context={"recipe": recipe})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect("/login")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid credentials")
            return redirect("/login")

        else:
            login(request=request, user=user)
            return redirect("/recipe")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("/login")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, "User already exists")
            return redirect("/register")

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.success(request, "User created")
        return redirect("/register")
    return render(request, "resgister.html")
