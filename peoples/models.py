from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=100)


class Worker(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    orders = models.ManyToManyField(Client, through='Order')


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    extra_price = models.IntegerField()


class Food(models.Model):
    name = models.CharField(max_length=100)
    start_price = models.IntegerField()
    orders = models.ManyToManyField(Ingredient, through='Order')


class Order(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateField()