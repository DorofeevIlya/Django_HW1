from datetime import date
from django.core.management.base import BaseCommand
from hw1app.models import Client
class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        client = Client(name='Banan', email='john@example.com',
        number='8912345678', address='Russia, Moscow', date_of_registration=date.today())
        client.save()
        self.stdout.write(f'{client}')
