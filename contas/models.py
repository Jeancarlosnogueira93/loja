from django.db import models


#Para criar banco de dados conforme a tipo de dados.

class categoria(models.Model):

    name = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.name


class transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length = 255)
    valor = models.DecimalField(max_digits=7,decimal_places =2)
    categoria = models.ForeignKey(categoria, on_delete = models.CASCADE)
    obs = models.TextField(null= True, blank = True)
    #Classe para alterar o neme de exibição.
    class Meta:
        verbose_name_plural = 'Trasações'
    
    def __str__(self) -> str:
        return self.descricao
    