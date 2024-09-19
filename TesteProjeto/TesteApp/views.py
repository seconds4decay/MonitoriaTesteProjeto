from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth import authenticate, login as lg
from django.contrib.auth.models import User

from TesteApp.models import Loja

class HomeView(View):
    def get(self, request):
        nome = request.user.username
        context = {"nome": nome}
        return render(request, 'home.html', context)
    
class CadastroView(View):
    def get(self, request):
        return render(request, 'cadastro.html')
    
    def post(sef, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        CadastroView.criarUsuario(username, email, password)
        return redirect('home')

    def criarUsuario(username, email, password):
        if CadastroView.obterUsuarioPorNome(username) is not None:
            raise ValueError("Usuário já existe")
        else:
            user = User.objects.create_user(username, email, password)
            user.save()

    def obterUsuarioPorNome(name):
        return User.objects.filter(username=name).first()
    

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        LoginView.loginUsuario(request, username, password)
        return redirect('home')

    def loginUsuario(request, username, password):
        user = authenticate(username=username, password=password)

        if user is None:
            raise ValueError("Usuário ou senha inválidos")
        else:
            lg(request, user)
            return
       
class CadastroLojaView(View):
    def get(self, request):
        return render(request, 'cadastroloja.html')
    
    def post(self, request):
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')

        CadastroLojaView.criarLoja(nome, endereco, telefone)
        return redirect('home')
    
    def criarLoja(nome, endereco, telefone):
        loja = Loja(nome=nome, endereco=endereco, telefone=telefone)
        loja.save()

class LojaViews(View):
    def get(self, request):
        lojas = Loja.objects.all()
        context = {"lojas": lojas}
        return render(request, 'lojas.html', context)