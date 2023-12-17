from django.forms import ModelForm
from .models import transacao

class transacaoform(ModelForm):
    class Meta:
        model = transacao
        fields = ['data', 'descricao', 'valor','categoria', 'obs'] 