from django.urls import path
from .views import (
    ClientSignUpView,
    FreelanceSignUpView,
    CustomAuthToken,
    LogoutView,
    ClientDashboard,
    FreelancerDashboard,
)

urlpatterns = [
    path("client/sign_up/", ClientSignUpView.as_view()),
    path("freelancer/sign_up/", FreelanceSignUpView.as_view()),
    path("login", CustomAuthToken.as_view()),
    path("logout", LogoutView.as_view()),
    path("client_dash", ClientDashboard.as_view()),
    path("freelancer_dash", FreelancerDashboard.as_view()),
]
