from django.shortcuts import render, redirect
from .models import Shoes
from .forms import ShoesForm

def index(requests):
    shoes = Shoes.objects.all()
    return render(requests, 'main/index.html', {'title': 'Главная страница сайта', 'Shoes': shoes})



def about(requests):
    return render(requests, 'main/about.html')

def Kfashion(requests):
    return render(requests, 'main/Kfashion.html')

def Jfashion(requests):
    return render(requests, 'main/Jfashion.html')

def minimalist(requests):
    return render(requests, 'main/minimalist.html')

def techwear(requests):
    return render(requests, 'main/techwear.html')

def streetwear(requests):
    return render(requests, 'main/streetwear.html')

def gorpcore(requests):
    return render(requests, 'main/gorpcore.html')
def shoes_str(requests):
    return render(requests, 'main/shoes_str.html')
def brands(requests):
    return render(requests, 'main/brands.html')

def shoes(requests):
    error = ''
    if requests.method == 'POST':
        form = ShoesForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ShoesForm()
    context = {
            'form': form,
            'error': error
    }

    form = ShoesForm()
    context = {
        'form': form
    }
    return render(requests, 'main/shoes.html', context)