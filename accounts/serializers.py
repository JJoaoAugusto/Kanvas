from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Account
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_superuser'] = user.is_superuser
        return token
    username = serializers.CharField()
    password = serializers.CharField()


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'password', 'is_superuser']
        extra_kwargs = {
            'id': {'read_only': True},
            "is_superuser": {"default": False},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        if validated_data["is_superuser"]:
            return Account.objects.create_superuser(**validated_data)
        else:
            return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance
