from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from apps.contas.forms import CustomUserCreationForm
from django.contrib.auth.models import Group, User
from django.contrib.auth import logout




#Rota de Timeout (Desconectado por inatividade)
def timeout_view(request):
    return render(request, 'contas/timeout.html')


def logout_view(request):
    logout(request)
    return redirect('home')

#Login
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email ou senha inválidos')
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'contas/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.is_valid = False
            usuario.save()

            group = Group.objects.get(name='Usuário')
            usuario.groups.add(group)

            messages.success(request, 'Registrado. Agora faça o login para começar!')
            return redirect('login')
        else:
            # Tratar quando usuario já existe, senhas... etc...
            messages.error(request, 'A senha deve ter pelo menos 1 caractere maiúsculo, \
                1 caractere especial e no minimo 8 caracteres.')
    form = CustomUserCreationForm()
    return render(request, "contas/register.html", {"form": form})
