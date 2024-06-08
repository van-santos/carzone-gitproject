from django.shortcuts import render
from pages.models import Team
# Create your views here.


# Aprendi  a trazer dados do meu banco de dados atraves das views

# faz uma funçao para puxar o template
def home(request):
    return render(request, 'pages/home.html')



def about(request):
    # criar uma instancia do objeto team e retornar no dicionario data
    teams = Team.objects.all()
    data = { 'teams': teams,
        }
    return render(request, 'pages/about.html', data)



def car(request):
    return render(request, 'pages/car.html')



def cardetails(request):
    return render(request, 'pages/car-details.html')



def blog(request):
    return render(request, 'pages/blog.html')



def blogdetails(request):
    return render(request, 'pages/blog-details.html')



def contact(request):
    return render(request, 'pages/contact.html')
