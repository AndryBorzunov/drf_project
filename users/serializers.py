from rest_framework import serializers

from users.models import Payment, User


# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ("email", "password", "password2", "phone", "city", "avatar")
#         extra_kwargs = {"password": {"write_only": True}}
#
#     def validate(self, data):
#         if data["password"] != data["password2"]:
#             raise serializers.ValidationError({"password": "Пароли не совпадают!"})
#         return data
#
#     def create(self, validated_data):
#         # Удаляем подтверждение пароля
#         validated_data.pop("password2")
#
#         user = User(email=validated_data["email"])
#         user.set_password(validated_data["password"])
#         user.save()
#
#         return user


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        #fields = ("id", "email", "username", "phone", "city", "avatar")


class UserPaymentHistorySerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "username", "phone", "city", "avatar", "payments")
