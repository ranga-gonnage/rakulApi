from django.urls import path
from users.views import RegisterApi
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
	path("signup/", RegisterApi.as_view()),
	path("login/", TokenObtainPairView.as_view(), name="login"),
	]