from django.shortcuts import render,redirect
from . import forms
#from .models import Customer,RoomManager
#from django.contrib.auth.hashers import make_password,check_password
#from django.contrib import messages
from django.shortcuts import redirect, render

#from django.conf import settings
from django.contrib.auth import login, authenticate, logout, get_user_model
#from django.contrib.auth.decorators import login_required
#mesages.info(request,'mail taken')

#######################################
def user_login(request):
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.session.get('username',None) and request.session.get('type',None)=='manager':
        return redirect('manager_dashboard')
    if request.method == 'POST':
        # On recupère les données dans l'instance du formulaire
        form = forms.LoginForm(request.POST)
        #Verifie si le formulaire est valide
        if form.is_valid():
            #On authentifie l'instance du user avec la methode authenticate
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            #Test si le usernme  envoyé du fomrulair ,'est pas null
            if user is not None:
                #Etablie une connection de lutilisateur
                login(request, user)
                #On le redirige vers une page ici c'est index.html
                return redirect('user_login')
            #si le formulaire n'est pas correct e.i si des les données dont incorrecte informé le user
        message = 'Identifiants invalides.'
    return render(request, 'login/user_login.html', context={'form': form, 'message': message})
    
##################################################
def manager_login(request):
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.session.get('username',None) and request.session.get('type',None)=='manager':
        return redirect('manager_dashboard')
    if request.method == 'POST':
        # On recupère les données dans l'instance du formulaire
        form = forms.LoginForm(request.POST)
        #Verifie si le formulaire est valide
        if form.is_valid():
            #On authentifie l'instance du user avec la methode authenticate
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            #Test si le usernme  envoyé du fomrulair ,'est pas null
            if user is not None:
                #Etablie une connection de lutilisateur
                login(request, user)
                #On le redirige vers une page ici c'est index.html
                return redirect('manager_login')
            #si le formulaire n'est pas correct e.i si des les données dont incorrecte informé le user
        message = 'Identifiants invalides.'
    return render(request,'login/manager_login.html',{})
############################################
def user_signup(request):
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.session.get('username',None) and request.session.get('type',None)=='manager':
        return redirect('manager_dashboard')
    #crée une instance du formulaire
    form = forms.RegisterCustomerForm()
    #Test l'action si post (envoi de donnée)
    if request.method == 'POST':
        # On recupère les données dans l'instance du formulaire
        form = forms.RegisterRoomManagerForm(request.POST, request.FILES)
        #Verifie si le formulaire est valide
        if form.is_valid():
            #sauvegarde
            user = form.save()
            # auto-login user
            login(request, user)
            #return redirect(settings.LOGIN_REDIRECT_URL)
            redirect('user_signup')
    return render(request,'login/user_login.html',{})
###################################################################
def manager_signup(request):
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.session.get('username',None) and request.session.get('type',None)=='manager':
        return redirect('manager_dashboard')
    if request.session.get('username',None) and request.session.get('type',None)=='manager':
        return redirect('manager_dashboard')
    #crée une instance du formulaire
    form = forms.RegisterRoomManagerForm()
    #Test l'action si post (envoi de donnée)
    if request.method == 'POST':
        # On recupère les données dans l'instance du formulaire
        form = forms.RegisterRoomManagerForm(request.POST, request.FILES)
        #Verifie si le formulaire est valide
        if form.is_valid():
            #sauvegarde
            user = form.save()
            # auto-login user
            login(request, user)
            #return redirect(settings.LOGIN_REDIRECT_URL)
            #redirect('user_signup')
            redirect('manager_signup')
    return render(request,'login/manager_login.html',{})

###############################
def logout(request):
    if request.session.get('username', None):
        del request.session['username']
        del request.session['type']
        return render(request,"login/logout.html",{})
    else:
        return render(request,"login/user_login.html",{})


