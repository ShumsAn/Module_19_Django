from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator

# Create your views here.

users = Buyer.objects.all()


# Create your views here.
def main_page(request):
    page_name = "Главная страница"
    context = {'page_name': page_name}
    return render(request, 'platform.html',context)

def game_page(request):
    page_name = "Игры"
    games = Game.objects.all()
    context = {
        'games': games,
        'page_name': page_name
    }
    return render(request, 'games.html',context)

def cart_page(request):
    page_name = "Корзина"
    content = "Ваша корзина пуста"
    context = {'page_name': page_name,
               'content': content}
    return render(request, 'cart.html', context)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if Buyer.objects.filter(name=username).exists():
            info['error'] = 'Пользователь уже существует'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            info['success'] = f'Приветствуем, {username}!'
            Buyer.objects.create(name=username,balance=0,age=age)


    info['form'] = UserRegister()
    return render(request, 'registration_page.html',info)

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if Buyer.objects.filter(name=username).exists():
            info['error'] = 'Пользователь уже существует'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            info['success'] = f'Приветствуем, {username}!'
            Buyer.objects.create(name=username, balance=0, age=age)

    info['form'] = UserRegister()
    return render(request, 'registration_page.html', info)


def news(request):
    # получаем все новости c сортировкой по дате
    all_news = News.objects.all().order_by('-date')
    # создаем пагинатор
    paginator = Paginator(all_news, 10)  # 10 новостей на странице
    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')
    # получаем новости для текущей страницы
    news = paginator.get_page(page_number)
    # передаем контекст в шаблон
    return render(request, 'news.html', {'news': news})

