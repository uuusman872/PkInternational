from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("team", views.our_team, name="team"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("search", views.search, name="search")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
