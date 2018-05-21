from django.urls import path, include


from .views import *

app_name = 'accounts'

urlpatterns = [
    path(r'profile/edit/', ProfileView.as_view(), name='edit_profile'),
    path(r'profile/<option>/', ProfileView.as_view(), name='profile'),
    path(r'applicant/<int:pk>/', ApplicantView.as_view(), name='applicant'),
    path(r'login/', loginView.as_view(), name='login'),
    path(r'logout/', sign_out, name='logout'),
    path(r'signup/', SignupView.as_view(), name='signup'),



]
