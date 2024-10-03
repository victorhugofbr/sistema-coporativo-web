from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "messagem": messages.success(request, 'Esta é uma mensagem de sucesso!')
    }
    return render(request, 'pages/index.html',context)