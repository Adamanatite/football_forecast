from django.urls import path
from forecast_app import views

app_name = "forecast_app"

urlpatterns = [
    path("", views.homepage, name="home"),
]