from django.shortcuts import render

# Create your views here.


# faz uma funçao para puxar o template
def home(request):
    return render(request, 'pages/home.html')



def about(request):
    return render(request, 'pages/about.html')



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
