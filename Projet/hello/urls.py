from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("liste_invites/", views.liste_invites, name="liste_invites"),
    path('saisie-donnees/', views.saisie_donnees_invite, name='saisie_donnees_invite'),
]
