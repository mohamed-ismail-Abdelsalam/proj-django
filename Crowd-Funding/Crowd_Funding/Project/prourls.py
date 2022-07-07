from django.urls import path
from Project.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('Create/', pro),
    path('projects',show_projects),
    path('reports',reportss),
    path('Category/<category_name>', cartegory)

]