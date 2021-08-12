from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from datetime import timedelta
from PIL import Image
import string, random

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    picture = models.ImageField(null=True, upload_to='profile_images', blank=True, default="player_default.png")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        picture = Image.open(self.picture.path)
        picture.save(self.picture.path, quality=40, optimize=True)

    def __str__(self):
        return self.user.username


class Team(models.Model):
    name = models.CharField(max_length=50, null=False)
    abbreviation = models.CharField(max_length=3, null=False)
    logo = models.ImageField(null=True, upload_to='team_images', blank=True, default="team_default.png")
    colour = models.CharField(max_length=7, default="#8e918f")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        logo = Image.open(self.logo.path)
        logo.save(self.logo.path, quality=40, optimize=True)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=50, null=False)
    tour_slug = models.SlugField(max_length=50, default="")
    picture = models.ImageField(null=True, upload_to='tournament_images', blank=True, default="tournament_default.png")
    colour = models.CharField(max_length=7, default="#8e918f")
    start = models.DateTimeField('start date', default=timezone.now)
    end = models.DateTimeField('end date', default=timezone.now)
    winner = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.tour_slug = slugify(self.name)
        super().save(*args, **kwargs)
        picture = Image.open(self.picture.path)
        picture.save(self.picture.path, quality=40, optimize=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_team")
    away = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_team")
    start = models.DateTimeField('start date', default=timezone.now)
    round = models.CharField(max_length=30, null=True)
    home_goals = models.IntegerField(default=0)
    away_goals = models.IntegerField(default=0)

    def __str__(self):
        return self.home.abbreviation + " vs " + self.away.abbreviation + " (" + self.start + ")"

    class Meta:
        verbose_name_plural = 'Matches'


class League(models.Model):
    league_id = models.SlugField(primary_key=True, unique=True, editable=False, blank=True)
    name = models.CharField(max_length=30, null=False)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=False)

    # Adapted from https://stackoverflow.com/a/3830523
    def save(self, *args, **kwargs):
        while not self.league_id:
            newslug = ''.join([
                random.sample(string.letters, 4),
                random.sample(string.digits, 3),
            ])

            if not self.objects.filter(pk=newslug).exists():
                self.league_id = newslug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CompetesIn(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=False)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)


class PlaysIn(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    league = models.ForeignKey(League, on_delete=models.CASCADE, null=False)
    isOwner = models.BooleanField(default=False)


class Predicts(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=False)
    home_goals = models.IntegerField(null=False)
    away_goals = models.IntegerField(null=False)


