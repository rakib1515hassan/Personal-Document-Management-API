from django.urls import path
from Account import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Verify The Token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
     

    path('register/', views.UserRegistrationView.as_view(), name='UserRegistrationView'),
    path('login/', views.UserLoginView.as_view(), name='UserLoginView'),
    path('profile/', views.UserProfileView.as_view(), name='UserProfileView'),
    path('change-password/', views.UserChangePasswordView.as_view(), name='UserChangePasswordView'),
    path('reset-password-email-send/', views.SendPasswordResetEmailView.as_view(), name='SendPasswordResetEmailView'),
    path('reset-password-email-verify/', views.UserPasswordResetView.as_view(), name='UserPasswordResetSerializer'),

]

