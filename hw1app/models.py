from django.core.validators import MinValueValidator
from datetime import timedelta
from django.utils import timezone
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField()
    address = models.CharField(max_length=100)
    date_of_registration = models.DateField()

    def __str__(self):
        return f'{self.name}, {self.email}, {self.number}, {self.address}, {self.date_of_registration}'

class Goods(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_of_add = models.DateField()
    image = models.ImageField(upload_to='',null=True, blank=True)

    def __str__(self):
        return f'Title: {self.title} add'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Goods)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    @classmethod
    def orders_by_time_delta(cls, user_id, days):
        time_delta = timedelta(days=days)
        today = timezone.now().date()
        orders = Order.objects.filter(date_ordered__date__range=[today - time_delta, today], client_id=user_id)
        return orders

    def add_product(self, product):
        if product in self.products.all():
            existing_product = self.products.get(pk=product.pk)
            existing_product.quantity += product.quantity
            existing_product.save()
        else:
            self.products.add(product)

        self.total_price += product.price
        return

    @staticmethod
    def get_total_products(orders):
        #возвращаем словарь содержащий id продукта и его общее количество в списке заказов
        total_products = {}
        for order in orders:
            for product in order.products.all():
                total_products[product.id] = total_products.setdefault(product.id, 0)+product.quantity

        return total_products

    def __str__(self):
        return f"Order {self.id} by {self.client.name}"








