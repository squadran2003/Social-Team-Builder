from django.urls import path, include
from .views import (ProfileView, ApplicantView,
                    loginView, sign_out, SignupView)

app_name = 'accounts'

urlpatterns = [
    path('profile/edit/', ProfileView.as_view(), name='edit_profile'),
    path('profile/<option>/', ProfileView.as_view(), name='profile'),
    path('applicant/<int:pk>/', ApplicantView.as_view(), name='applicant'),
    path('login/', loginView.as_view(), name='login'),
    path('logout/', sign_out, name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),



]
