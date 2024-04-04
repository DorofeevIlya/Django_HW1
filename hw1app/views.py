import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


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
