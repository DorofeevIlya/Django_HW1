from datetime import date

from django.core.management.base import BaseCommand
from hw1app.models import Goods
class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        goods = Goods(title='Apple', description='home, sweet', price=10,
                      quantity=15, date_of_add=date.today())
        goods.save()
        self.stdout.write(f'{goods}')