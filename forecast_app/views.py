from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from forecast_app.forms import UserForm
from forecast_app.models import UserProfile
from django.http import HttpResponseRedirect

# Create your views here.
def homepage(request):
    # Create response render
    response = render(request, 'forecast_app/home.html')
    return response


def login_view(request):
    if request.method == 'POST':
        #Get form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Check credentials
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('forecast_app:home'))
            else:
                #Re-render login page with error if account disabled
                return render(request, 'forecast_app/login.html',
                context={"error": "Your account is disabled."})
        else:
            # Re-render login page with error if password doesn't match
            return render(request, 'forecast_app/login.html', context = {"error": "Your username and password don't match, try again"})
    else:
        return render(request, 'forecast_app/login.html')


def register(request):
    registered = False

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            new_user.set_password(new_user.password)
            new_user.save()

            profile = UserProfile.objects.get_or_create(user=new_user)[0]
            if not profile.picture:
                profile.picture = 'player_default.png'
                profile.save()

            registered = True
            login(request, new_user)

            return HttpResponseRedirect(request.POST.get('next') or reverse('forecast_app:home'))

    else:
        form = UserForm()

    # Create response render
    response = render(request, 'forecast_app/register.html', {"form": form})
    return response


def player(request, player_id):
    context_dict = {"player_id": player_id}
    # Create response render
    response = render(request, 'forecast_app/player.html', context=context_dict)
    return response


def league_create(request):
    # Create response render
    response = render(request, 'forecast_app/league_create.html')
    return response


def league_join(request, league_id):
    context_dict = {"league_id": league_id}
    # Create response render
    response = render(request, 'forecast_app/league.html', context=context_dict)
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


