from django.urls import path, include


from .views import *

app_name = 'applications'

urlpatterns = [
    path(r'add/<int:project_id>/<int:position_id>/',CreateApplicationView.as_view(), name='add'),
]