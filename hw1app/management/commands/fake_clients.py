from datetime import date
from django.core.management.base import BaseCommand
from hw1app.models import Client, Order, Goods

class Command(BaseCommand):
    help = "Generate fake clients and orders."
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name{i}', email=f'email{i}@example.com',
            number=f'{i}12345678{i}', address=f'Russia, Moscow, st. Lenina {i}', date_of_registration=date.today())
            client.save()
            for j in range(1, count + 1):
                order = Order(customer=Client.id, products=Goods.title, total_price=Goods.price, date_ordered =date.today())
                order.save()
