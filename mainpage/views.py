from django.shortcuts import render,redirect
from .models import *
from . forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def index(request):
    products = ProductName.objects.all()
    form = SearchForm()

    if request.method == 'POST':
        find_product = request.POST.get('search_product')
        product_find = ProductName.objects.get(name=find_product)

        return product_info(request, product_find.id)
        #HttpResponse(f'{product_find.name}  Описание: {product_find.about}, Цена: {product_find.price}')

    else:
        context = {'products':products, 'form':form}
        return render(request, 'main_page/index.html', context)

def product_info(request, pk):
    products = ProductName.objects.get(id=pk)

    context = {'products': products}
    return render(request, 'main_page/product_info.html', context)

# Функция регистрации
def register(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = UserCreationForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return redirect('/')
    else: # Иначе
        # Создаём форму
        form = UserCreationForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'main_page/register.html', data)