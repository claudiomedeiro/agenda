from django.shortcuts import render
from core.models import Evento

# Create your views here.
def lista_eventos(request):
    usuario = request.user
    # evento = Evento.objects.get(id=1)     # pega um específico
    evento = Evento.objects.all()         # pega todos
    # evento = Evento.objects.filter(usuario=usuario)# pega de usuário específico
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)