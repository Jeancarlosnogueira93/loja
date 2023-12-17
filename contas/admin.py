from django.contrib import admin
from .models import categoria
from .models import transacao

#Criar registros no banco de dados.
admin.site.register(categoria)
admin.site.register(transacao)