from django.contrib import admin
from django.urls import path
from Admin.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('Slider', sliders),
    path('Featured',Featurd),
    path('slider/delete/<int:list_id>', delete),
    path('Feat/delete/<int:list_id>', deletefeate)

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
