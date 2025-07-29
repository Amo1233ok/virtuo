from django.shortcuts import render,redirect

from .forms import RequeteForm

from django.core.mail import send_mail

from .models import Requete
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, "website/index.html")

def send_request(request):
    if request.method == 'POST':
        nom = request.POST.get('Nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        objet = request.POST.get('objet')
        content = request.POST.get('message')

        if not email:
            email = "Veuillez fournir un email"

        if not content:
            content = "Veuillez fournir un message"

        new_requete = Requete.objects.create(
                Nom=nom, 
                telephone=telephone, 
                email=email, 
                objet=objet, 
                message=content
            )
        new_requete.save()

        if new_requete:
            send_mail(
                objet,
                content,
                "amononperou@gmail.com",
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Votre requete a ete soumise avec succes !')
            return render(request, 'website/index.html', {}) 

        messages.error(request, 'Impossible de soumettre votre requete.')
        return render(request, 'website/index.html', {}) 

    return render(request, 'website/index.html', {}) 
            

