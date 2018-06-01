from django.urls import path, include


from .views import (CreateProjectView, ProjectDeleteView,
                    ProjectUpdateView, ProjectDetailView,
                    PositionFilterView, PositionSearchView)

app_name = 'projects'

urlpatterns = [
    path('add/', CreateProjectView.as_view(), name='add'),
    path('detail/<int:pk>/', ProjectDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', ProjectUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='delete'),
    path('filter/<filter>/', PositionFilterView.as_view(), name='filter'),
    path('search/', PositionSearchView.as_view(), name='search'),



]