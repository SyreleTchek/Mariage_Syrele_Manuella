from django.shortcuts import render
from django.utils.timezone import datetime
from django.shortcuts import redirect
from hello.forms import InvitesForm
from hello.models import Invite
from django.core.mail import send_mail

def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def liste_invites(request):
    invites = Invite.objects.all()
    form = InvitesForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('hello/liste_invites.html')  # Redirection vers la liste des invités après ajout
    return render(request, 'hello/liste_invites.html', {'invites': invites, 'form': form})

def saisie_donnees_invite(request):
    if request.method == 'POST':
        form = InvitesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)  # Enregistrement des données du formulaire dans la base de données
            presence_confirme = form.cleaned_data.get('presence_confirme')  # Accès à la valeur de presence_confirme
            instance.save()  # Enregistrement complet après accès au champ presence_confirme
            # Envoi de l'e-mail de notification basé sur la valeur de presence_confirme
            if presence_confirme:
                send_confirmation_email(instance.email, instance.prenom)
            else:
                send_non_confirmation_email(instance.email, instance.prenom)
            return render(request, 'hello/saisie_donnees_invite.html', {'form': form })  # Redirection vers une page de confirmation
    else:
        form = InvitesForm()

    return render(request, 'hello/saisie_donnees_invite.html', {'form': form})

def send_non_confirmation_email(email, nom_invite):
    subject = 'Mariage Syrele & Manuella'
    message = f"Cher(e) {nom_invite},\n\nMerci pour votre Enregistrement. Neamoins nous attendons votre confirmation finale. Nous sommes impatients de vous voir à notre mariage !\n\nCordialement,\nSyrele & Manu"
    sender_email = 'tsyrele@gmail.com'  # Remplacez par votre adresse e-mail
    send_mail(subject, message, sender_email, [email])
    pass

def send_confirmation_email(email, nom_invite):
    subject = 'Mariage Syrele & Manuella'
    message = f"Cher(e) {nom_invite},\n\nMerci pour votre confirmation. Nous sommes impatients de vous voir à notre mariage !\n\nCordialement,\nSyrele & Manu"
    sender_email = 'tsyreleqgmail.com'  # Remplacez par votre adresse e-mail
    send_mail(subject, message, sender_email, [email])