from django.urls import path, include
from accounts.views import CustomAuthToken, register

urlpatterns = [
    path('register/', register, name='register'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('login/', CustomAuthToken.as_view(), name='token_create'),
]