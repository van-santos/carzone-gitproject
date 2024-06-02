
# NOTE: Aqui nao sei bem o que aconteceu ele criou um url para o app pages
# e usou o modullo 'include' vou pesquisar depois



# ele falou sobre remover a pagina principal do django


from django.urls import path
from pages import views 

urlpatterns = [
    path('', views.home, name= 'home'),
]
