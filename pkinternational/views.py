from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils.translation import gettext, get_language, activate
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as userLogin

from .models import ContactModel


def home(request):
    trans = translate(language="jp")
    return render(request, "pages/home.html", {"trans": trans})


def our_team(request):
    return render(request, "pages/ourTeam.html")


def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        msg = request.POST.get("msg")
        if email and name:
            contact = ContactModel(email=email, name=name, msg=msg)
            contact.save()
            messages.info(request, f"Thanks for reaching us we will contact you soon")
    return render(request, "pages/contact.html")


def login(request):
    if request.method == "POST":
        print("[+] Login Post Form ")
        username = request.POST.get('username')
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            userLogin(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("home")
        else:
            messages.error(request, f"Account Does not exist's please sign up")
    return render(request, "pages/login.html")


def register(request):
    if request.method == "POST":
        print(f"[+] The data recived is {request.POST['username']}")
        username = request.POST.get('username')
        email = request.POST['email']
        password = request.POST['password']
        user = User(email=email, username=username, password=password)
        user.save()
        messages.info(request, f"Sign Up Complete")
        return redirect('login')

    return render(request, "pages/register.html")


def search(request):
    return render(request, "pages/search.html")


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = _("hello")
    except Exception as e:
        print(e)
    finally:
        activate(cur_language)
    return text


from django.http import HttpResponse
from django.utils.translation import gettext as _


def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)
