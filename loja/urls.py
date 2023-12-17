from django.contrib import admin
from django.urls import path
#exportar a funções para urls
from contas.views import home, listagem, nova_transacao, update , delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listagem, name = 'url_listagem'),
    path('home/', home),
    path('update/<int:pk>/',update,name='url_update'),
    path('insert/', nova_transacao, name = 'url_nova'),
    path('delete/<int:pk>/',delete, name='url_delete')
]
