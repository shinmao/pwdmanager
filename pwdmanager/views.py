from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from .models import Secret
from django.contrib.auth.models import User
from .forms import SecretForm

def secret_store(request):
    if request.method == 'POST':
        form = SecretForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            idem = User.objects.only('email').get(email=request.user.email)
            f_website = form.cleaned_data['website']
            f_username = form.cleaned_data['username']
            f_email = form.cleaned_data['email']
            f_password = form.cleaned_data['password']
            f_notes = form.cleaned_data['notes']
            
            new_secret = Secret.objects.create(idEmail=idem, website=f_website, username=f_username, email=f_email, password=f_password, notes=f_notes, build_date=datetime.now())
            secret_message = 'Congrats to store new scret'
            return render(request, 'account/email.html', {'secret_message': secret_message})
        else:
            return HttpResponse("Your input is not valid or you are not authenticated!")
    else:
        form = SecretForm()
    return render(request, 'account/secret_store.html', {'form': form})
