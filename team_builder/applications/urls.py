from django.urls import path
from .views import (ListApplicationView,
                    CreateApplicationView,
                    EditApplicationView,
                    ApplicationFilterView)

app_name = 'applications'

urlpatterns = [
    path(r'add/<int:project_id>/<int:position_id>/', 
         CreateApplicationView.as_view(), name='add'),
    path(r'edit/<int:pk>/', EditApplicationView.as_view(), name='edit'),
    path(r'', ListApplicationView.as_view(), name='list'),
    path('filter/<filter>/', ApplicationFilterView.as_view(), name='filter'),
]