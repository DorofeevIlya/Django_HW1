import logging

from django.http import HttpResponse, HttpResponseRedirect

logger = logging.getLogger(__name__)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client, Goods, Order
from .forms import SelectGoods, GoodsForm, GoodsFormdel, ImageForm
from django.core.files.storage import FileSystemStorage



def index(request):
    logger.exception(f'Главная страница - работает')
    html = '<h1>Главная</h1>' \
           '<p> Самая главная страница на сайте </p>'
    return HttpResponse(html)


def about(request):
    logger.exception(f'Страница о себе - работает')
    html = '<h1>О себе</h1>' \
           '<p> Здесь будет информация о себе! </p>'
    return HttpResponse(html)


def show_orders(request, user_id):
    client = Client.objects.filter(id=user_id).first()
    if not client:
        return HttpResponse('<h3> Пользователь с указанным ID не найден </h3>')

    orders = Order.objects.filter(client_id=user_id).all()
    context = {'orders': orders, 'user_id': user_id, 'user_name': client.name}
    return render(request, 'hw1app/orders_filter.html', context)

def orders_total(request, user_id, interval):
    client = Client.objects.filter(id=user_id).first()
    if not client:
        return HttpResponse('<h3> Пользователь с указанным ID не найден </h3>')

    INTERVALS = {'week': 7, 'month': 30, 'year': 365}
    if interval not in INTERVALS.keys():
        return HttpResponse('<h3> Такого интервала не существует. Выберите week, month или year </h3>')

    orders = Order.orders_by_time_delta(user_id, INTERVALS[interval])
    total_products = Order.get_total_products(orders)
    products = Goods.objects.filter(id__in=total_products.keys())

    context = {'orders': orders, 'products' : products, 'total_products':total_products,
               'user_id': user_id, 'user_name': client.name}
    return render(request, 'hw1app/orders_filter.html', context)



def select_an_action(request):
    if request.method == 'POST':
        form = SelectGoods(request.POST)
        if form.is_valid():
            select = form.cleaned_data['select']
            if form == 'add':
                return add_goods(request)
            elif form == 'put':
                return "put"
            elif form == 'del':
                return "del"
    else:
        form = SelectGoods()
    return render(request, 'hw1app/select_an_action.html', {'form': form})


def add_goods(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            date_of_add = form.cleaned_data['date_of_add']
            good = Goods(title=title, description=description, price=price, quantity=quantity, date_of_add=date_of_add)
            good.save()
            form = GoodsForm()
            message = 'Данные сохранены'
            return render(request, 'hw1app/add_goods.html', {'form':form, 'message': message})
    else:
        form = GoodsForm()
        message = 'Введите данные'
    return render(request, 'hw1app/add_goods.html', {'form': form, 'message': message})

def del_goods(request):
    if request.method == 'POST':
        form = GoodsFormdel(request.POST)
        good = Goods.objects.first()
        print(good.title)
        if form.is_valid():
            id = form.cleaned_data['id']
            good.delete()
        if not good:
            return HttpResponse('Пользователь с указанным ID не найден')
    else:
        form = GoodsFormdel()
        message = 'Введите данные'
    return render(request, 'hw1app/del_goods.html', {'form': form, 'message': message})


def del_good(request):
    if request.method == 'POST':
        form = GoodsFormdel(request.POST)
        doog_id = request.POST.get('doog_id')
        pk = Order.objects.filter(pk=doog_id).first()
        if form.is_valid():
            pk = form.cleaned_data['pk']
            pk.delete()
    else:
        form = GoodsFormdel()
        return render(request, 'hw1app/del_goods.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'hw1app/upload_image.html', {'form': form})


def add_images(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
        form = GoodsForm()
        message = 'Данные сохранены'
        return render(request, 'hw1app/add_goods.html', {'form':form})
    else:
        form = GoodsForm()
        message = 'Введите данные'
    return render(request, 'hw1app/add_goods.html', {'form': form})