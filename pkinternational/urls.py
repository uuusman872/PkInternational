from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls.i18n import i18n_patterns

admin.site.site_header = "株式会社 PK INTERNATIONAL Admin"
admin.site.site_title = "株式会社 PK INTERNATIONAL Admin Portal"
admin.site.index_title = "Welcome to 株式会社 PK INTERNATIONAL Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("team", views.our_team, name="team"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("search", views.search, name="search"),
    path("sell", views.sell, name="sell"),
    path("about", views.about, name="about"),
    path("cars_list_view", views.cars_list_view, name="cars_list_view")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 