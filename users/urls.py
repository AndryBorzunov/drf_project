from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    CustomTokenObtainPairView,
    PaymentCreateAPIView,
    PaymentDestroyAPIView,
    PaymentListAPIView,
    PaymentRetrieveAPIView,
    PaymentSuccessAPIView,
    PaymentUpdateAPIView,
    UserCreateAPIView,
    UserDestroyAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    # users
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        CustomTokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("", UserListAPIView.as_view(), name="users_list"),
    path("users/<int:pk>/", UserRetrieveAPIView.as_view(), name="users_retrieve"),
    path("users/<int:pk>/update/", UserUpdateAPIView.as_view(), name="users_update"),
    path("users/<int:pk>/delete/", UserDestroyAPIView.as_view(), name="users_delete"),
    # payments
    path("payments/", PaymentListAPIView.as_view(), name="payments_list"),
    path(
        "payments/<int:pk>", PaymentRetrieveAPIView.as_view(), name="payments_retrieve"
    ),
    path("payments/create/", PaymentCreateAPIView.as_view(), name="payments_create"),
    path(
        "payments/<int:pk>/delete/",
        PaymentDestroyAPIView.as_view(),
        name="payments_delete",
    ),
    path(
        "payments/<int:pk>/update/",
        PaymentUpdateAPIView.as_view(),
        name="payments_update",
    ),
    path("payment/success/", PaymentSuccessAPIView.as_view(), name="payment_success"),
]
