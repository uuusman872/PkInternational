from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import gettext, get_language, activate


def home(request):
    trans = translate(language="jp")
    return render(request, "pages/home.html", {"trans": trans})


def our_team(request):
    return render(request, "pages/ourTeam.html")


def contact(request):
    return render(request, "pages/contact.html")


def login(request):
    return render(request, "pages/login.html")


def register(request):
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
