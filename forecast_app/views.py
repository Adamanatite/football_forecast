from django.shortcuts import render


# Create your views here.
def homepage(request):
    # Create response render
    response = render(request, 'forecast_app/home.html')
    return response


def login(request):
    # Create response render
    response = render(request, 'forecast_app/login.html')
    return response


def register(request):
    # Create response render
    response = render(request, 'forecast_app/register.html')
    return response


def player(request, player_id):
    context_dict = {"player_id": player_id}
    # Create response render
    response = render(request, 'forecast_app/player.html', context=context_dict)
    return response


def league_join(request):
    # Create response render
    response = render(request, 'forecast_app/league_join.html')
    return response


def league(request, league_id):
    context_dict = {"league_id": league_id}
    # Create response render
    response = render(request, 'forecast_app/league.html', context=context_dict)
    return response


def tournaments(request):
    # Create response render
    response = render(request, 'forecast_app/tournaments.html')
    return response


def tournament_overview(request, tour_slug):
    context_dict = {"tour_slug": tour_slug}
    # Create response render
    response = render(request, 'forecast_app/tournament_page.html', context=context_dict)
    return response


def tournament_enter(request, tour_slug):
    context_dict = {"tour_slug": tour_slug}
    # Create response render
    response = render(request, 'forecast_app/tournament_enter.html', context=context_dict)
    return response


def tournament_predict(request, tour_slug):
    context_dict = {"tour_slug": tour_slug}
    # Create response render
    response = render(request, 'forecast_app/tournament_predict.html', context=context_dict)
    return response


