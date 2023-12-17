from django.shortcuts import render
from django.http import HttpResponse
import datetime


#Para buscar a pagina nos templates

def home(request):
    data = {}
    data ['transacao'] = ['JOAO','MARIA','ANNA']
    data ['now'] = datetime.datetime.now()
    #html = "<html><body> A hora é %s.</body></html>" % now
    return render(request, 'contas/home.html', data)