from django.urls import path, include


from .views import *

app_name = 'projects'

urlpatterns = [
    path(r'add/', CreateProjectView.as_view(), name='add'),
    path(r'detail/<int:pk>/', ProjectDetailView.as_view(), name='detail'),
    path(r'update/<int:pk>/', ProjectUpdateView.as_view(), name='update'),
    path(r'update/position/<int:pk>/', UpdatePositionAppliedStatus.as_view(), name='update-position'),
    path(r'filter/<filter>/',PositionFilterView.as_view(), name='filter'),
    path(r'search/',PositionSearchView.as_view(), name='search'),



]