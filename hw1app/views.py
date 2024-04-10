import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Goods, Order

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