
# NOTE: Aqui nao sei bem o que aconteceu ele criou um url para o app pages
# e usou o modullo 'include' vou pesquisar depois



# ele falou sobre remover a pagina principal do django


from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about', views.about, name= 'about'),
    path('contact', views.contact, name= 'contact'),
    path('blog', views.blog, name= 'blog'),
    path('blog-details', views.blogdetails, name= 'blog-details'),
    path('car', views.car, name= 'car'),
    path('car-details', views.cardetails, name= 'car-details'),


]
