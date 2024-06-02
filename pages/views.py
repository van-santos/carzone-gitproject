from django.shortcuts import render

# Create your views here.


# faz uma funçao para puxar o template
def home(request):
    return render(request, 'pages/home.html')
