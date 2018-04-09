from django.urls import path, include


from .views import *

app_name = 'projects'

urlpatterns = [
    path(r'add/', CreateProjectView.as_view(), name='add'),



]