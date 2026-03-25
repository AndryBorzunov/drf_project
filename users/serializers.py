from django.utils import timezone
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Payment, User


class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Обновляем last_login
        self.user.last_login = timezone.now()
        self.user.save(update_fields=["last_login"])

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# class LoginSerializer(UserSerializer):
#     email = serializers.CharField()
#     password = serializers.CharField(write_only=True)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserPaymentHistorySerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "username", "phone", "city", "avatar", "payments")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context["request"].user
        instance = self.instance

        # Убираем поля для чужого пользователя
        if instance and instance != user:
            self.fields.pop("payments", None)
