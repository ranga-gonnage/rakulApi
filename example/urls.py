from django.urls import path
from example.views import ExampleEndPoint


urlpatterns = [
	path("example/", ExampleEndPoint.as_view()),
	]