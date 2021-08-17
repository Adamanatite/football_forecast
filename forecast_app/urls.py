from django.urls import path
from forecast_app import views

app_name = "forecast_app"

urlpatterns = [
    path("", views.homepage, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("player/<int:player_id>/", views.player, name="player"),
    path("league/create/", views.league_create, name="league_create"),
    path("league/join/<int:league_id>", views.league_join, name="league_join"),
    path("league/<int:league_id>/", views.league, name="league"),
    path("tournaments/", views.tournaments, name="tournaments"),
    path("tournaments/<slug:tour_slug>/", views.tournament_overview, name="tournament_overview"),
    path("tournaments/<slug:tour_slug>/enter/", views.tournament_enter, name="tournament_enter"),
    path("tournaments/<slug:tour_slug>/predict/", views.tournament_predict, name="tournament_predict"),
]