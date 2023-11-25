from rest_framework.generics import CreateAPIView
from .models import Account
from .serializers import AccountSerializer, CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class AccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = []
    permission_classes = []
