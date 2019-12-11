from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.core.mail import send_mail

from .models import Secret
from django.contrib.auth.models import User
from .forms import SecretForm, SecretEditForm

def start_page(request):
    return render(request, 'account/base.html')

def secret_page(request):
    if request.user.is_authenticated:
        usr = User.objects.get(id=request.user.id)
        secret_id_website = usr.relate.all().values('id', 'website')
    return render(request, 'account/secret_page.html', {'secret_id_website': secret_id_website})

def secret_edit(request, secret_id):
    if request.method == 'POST':
        form = SecretEditForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            usr = User.objects.get(id=request.user.id)
            related_secret_id = usr.relate.all().values('id')

            # convert the value list of secret id
            list_of_secid = []
            size_o_list = len(related_secret_id)
            for i in range(0, size_o_list):
                list_of_secid.append(related_secret_id[i]['id'])

            if secret_id in list_of_secid:
                cur_secret = Secret.objects.get(id=secret_id)
                # first, send old secret by mail
                send_mail(
                        'Here is your old secret of '+cur_secret.get_site(),
                        'Nice to meet you! Here is Pwdmanager, you have been requested to change the old secret of ' + cur_secret.get_site() + ', make sure your old secret in this email: username: ' + cur_secret.get_username() + ', email: ' + cur_secret.get_email() + ', password: ' + cur_secret.get_password() + ', notes: ' + cur_secret.get_notes() + '. Good luck!',
                        'pwdmanager@example.com',
                        [ request.user.email ],
                        fail_silently=False,
                )

                # second, authenticate data from form
                f_username = form.cleaned_data['username']
                f_email = form.cleaned_data['email']
                f_password = form.cleaned_data['password']
                f_notes = form.cleaned_data['notes']

                Secret.objects.filter(id=secret_id).update(username=f_username, email=f_email, password=f_password, notes=f_notes, build_date=datetime.now())

                secret_message = "Successfully change your secret!"
                # return secret current user
                usr = User.objects.get(id=request.user.id)
                secret_id_website = usr.relate.all().values('id', 'website')
                return render(request, 'account/secret_page.html', {'secret_id_website': secret_id_website, 'secret_message': secret_message})
            else:
                return HttpResponse("You are only able to change your own secret!")
        else:
            return HttpResponse("Your input is not valid or you are not authenticated!")
    else:
        #website = Secret.objects.get(id=secret_id).values('website')
        secret_message = "Your old secret would be sent by the email!"
        form = SecretEditForm()
    return render(request, 'account/secret_edit.html', {'form': form, 'secret_message': secret_message})

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
            return render(request, 'account/secret_page.html', {'secret_message': secret_message})
        else:
            return HttpResponse("Your input is not valid or you are not authenticated!")
    else:
        form = SecretForm()
    return render(request, 'account/secret_store.html', {'form': form})
