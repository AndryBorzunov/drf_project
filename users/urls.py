from django.urls import path
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import UserViewSet, UserRegistrationView

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
]

urlpatterns += router.urls
