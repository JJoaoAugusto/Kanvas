from django.urls import path
from .views import AccountView, LoginJWTView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('accounts/', AccountView.as_view()),
    path('login/', LoginJWTView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view())
]