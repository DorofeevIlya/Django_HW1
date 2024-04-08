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
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_of_add = models.DateField()

    def __str__(self):
        return f'Title: {self.title} add'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Goods)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def calculate_total_amount(self):
        total = sum(goods.price *
                    goods.quantity for goods in self.products.all())
        self.total_amount = total
        self.save()

    def __str__(self):
        return f"Order {self.id} by {self.client.name}"








