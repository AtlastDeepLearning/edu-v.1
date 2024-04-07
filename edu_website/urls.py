from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name="home"),
    path('about.html', views.about, name="contact"),
    path('services.html', views.services, name="services"),
    path('why.html', views.why, name="why"),
    path('team.html', views.team, name="team")
]