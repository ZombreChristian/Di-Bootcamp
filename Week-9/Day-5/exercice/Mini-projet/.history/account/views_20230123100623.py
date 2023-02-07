from django.shortcuts import render,redirect
from .models import Customer,RoomManager
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
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
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if RoomManager.objects.filter(username=username):
            user=RoomManager.objects.filter(username=username)[0]
            password_hash=user.password
            res=check_password(password,password_hash)
            if res==1:
                request.session['username'] = username
                request.session['type'] = 'manager'
                return render(request,'booking/index.html',{})
            else:
                messages.warning(request,"Soit le Username ou password est incorrect")
                redirect('manager_login')
        else:
            messages.warning(request,"Désolé, aucun compte ne correspond à cet Username")
            redirect('manager_login')
    else:
        redirect('manager_login')
    return render(request,'login/manager_login.html',{})
############################################
def user_signup(request):
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.session.get('username',None) and request.session.get('type',None)=='manager':
        return redirect('manager_dashboard')
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        if Customer.objects.filter(username=username) or Customer.objects.filter(email=email):
           messages.warning(request,"Le compte exite déjà, svp veillez vous connectez pour continuer")
        else:
            password=request.POST['password']
            address=request.POST['address']
            pin_code=request.POST['pin_code']
            profile_pic=request.FILES.get('profile_pic',None)
            phone_no=request.POST['phone_no']
            state=request.POST['state']
            error=[]
            if(len(username)<3):
                error.append(1)
                messages.warning(request,"Le champ Username  doit dépassé 3 caractères.")
            if(len(password)<5):
                error.append(1)
                messages.warning(request,"Le champ Password doit dépassé 5 caractères.")
            if(len(email)==0):
                error.append(1)
                messages.warning(request,"Le champ Email ne doit pas être vide ")
            if(len(phone_no)!=10):
                error.append(1)
                messages.warning(request,"La taille du numéro doit atteindre 10 chiffres")
            if(len(error)==0):
                password_hash = make_password(password)
                customer=Customer(username=username,password=password_hash,email=email,phone_no=phone_no,address=address,state=state,pin_code=pin_code,profile_pic=profile_pic)
                customer.save()
                messages.info(request,"Votre compte a été crée avec succès!!! Successfully, veillez vous connectez pour continuer")
                redirect('user_signup')
            else:
                redirect('user_signup')
        
    else:
        redirect('user_signup')
    return render(request,'login/user_login.html',{})
###################################################################
def manager_signup(request):
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.session.get('username',None) and request.session.get('type',None)=='manager':
        return redirect('manager_dashboard')
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        if RoomManager.objects.filter(username=username) or RoomManager.objects.filter(email=email):
           messages.warning(request,"Le compte exite déjà, svp veillez vous connectez pour continuer")
        else:
            password=request.POST['password']
            profile_pic=request.FILES.get('profile_pic',None)
            phone_no=request.POST['phone_no']
            error=[]
            if(len(username)<3):
                error.append(1)
                messages.warning(request,"Le champ Username doit dépassé 3 caractères.")
            if(len(password)<5):
                error.append(1)
                messages.warning(request,"Le champ Password doit dépassé 5 caractères.")
            if(len(email)==0):
                error.append(1)
                messages.warning(request,"Le champ Email ne doit pas être vide ")
            if(len(phone_no)!=10):
                error.append(1)
                messages.warning(request,"La taille du numéro doit atteindre 10 chiffres")
            if(len(error)==0):
                password_hash = make_password(password)
                r_manager=RoomManager(username=username,password=password_hash,email=email,phone_no=phone_no,profile_pic=profile_pic)
                r_manager.save()
                messages.info(request,"Votre compte a été crée avec succès!!! Successfully, veillez vous connectez pour continuer")
                redirect('manager_signup')
            else:
                redirect('manager_signup')
        
    else:
        redirect('user_signup')
    return render(request,'login/manager_login.html',{})

###############################
def logout(request):
    if request.session.get('username', None):
        del request.session['username']
        del request.session['type']
        return render(request,"login/logout.html",{})
    else:
        return render(request,"login/user_login.html",{})


