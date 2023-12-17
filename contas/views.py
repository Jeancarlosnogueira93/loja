from django.shortcuts import render,redirect
from .models import transacao
from .form import transacaoform
import datetime

#Para buscar a pagina nos templates
def home(request):
    data = {}
    return render(request, 'contas/home.html', data)

#Criar uma listagem de dados
def listagem(request):
    data = {}
    data['transacao'] = transacao.objects.all()
    return render(request,'contas/listagem.html',data )

#insert no banco de dados 
def nova_transacao(request):
    data = {}
    form = transacaoform(request.POST or None)
    #validar os dados antes do input no banco
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form 
    return render(request, 'contas/form.html', data)

#Update no banco de dados 
def update(request, pk):
    data = {}
    Transacao = transacao.objects.get(pk=pk)
    form = transacaoform(request.POST or None, instance=Transacao)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form 
    data['transacao'] = Transacao
    return render(request, 'contas/form.html', data)

#delete dos dados no banco de dados.
def delete(request, pk):
    Transacao = transacao.objects.get(pk=pk)
    Transacao.delete()
    return redirect('url_listagem')
