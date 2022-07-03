from django.contrib import admin
from django.urls import path
from Users.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('register/', register),
    path('logout/', user_logout),
    path('login/', login),
    path('profile/', pro),
    path('home/', home, name="home"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         activate, name='activate'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
