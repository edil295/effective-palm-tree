from peoples.models import *

user1 = User(email='nikname21@gmail.com', password='defender42')
user1.save()
client = Client(name='Азат Соколов', user=user1, card_number='4147 5657 9878 9009')
client.save()
user2 = User(email='altywa1998@gmail.com', password='nono34')
user2.save()
worker = Worker(name='Алтынай Алиева', user=user2, position='Оператор кассы')
worker.save()
food1 = Food(name='Шаурма', start_price=50)
food2 = Food(name='Гамбургер', start_price=25)
ing1 = Ingredient(name='Сыр', extra_price=10)
ing2 = Ingredient(name='Курица', extra_price=70)
ing3 = Ingredient(name='Говядина', extra_price=80)
ing4 = Ingredient(name='Салат', extra_price=15)
ing5 = Ingredient(name='Фри', extra_price=15)
food1.save()
food2.save()
ing1.save()
ing2.save()
ing3.save()
ing4.save()
ing5.save()

order1 = Order(ingredient=ing3, food=food1, client=client, worker=worker, order_date_time='2022-08-15')
order2 = Order(ingredient=ing1, food=food1, client=client, worker=worker, order_date_time='2022-08-15')
order3 = Order(ingredient=ing4, food=food1, client=client, worker=worker, order_date_time='2022-08-15')
order4 = Order(ingredient=ing5, food=food1, client=client, worker=worker, order_date_time='2022-08-15')
order1.save()
order2.save()
order3.save()
order4.save()

order5 = Order(ingredient=ing2, food=food2, client=client, worker=worker, order_date_time='2022-08-16')
order5.save()
order5 = Order(ingredient=ing4, food=food2, client=client, worker=worker, order_date_time='2022-08-16')
order5.save()

# Выведите по отдельности стоимость: Шаурмы которую заказал Азат

f1 = Food.objects.all().get(name='Шаурма')

o1 = Order.objects.all().filter(food=f1)
num1 = 0
for z in o1:
    num1 = num1 + z.ingredient.extra_price

z1 = num1 + f1.start_price
print(z1)

#######################
# Выведите по отдельности стоимость: Гамбургера которую заказал Азат

f2 = Food.object.all().get(name='Гамбургер')

o2 = Order.objects.all().filter(food=f2)
num2 = 0

for z in o2:
    num2 = num2 + z.ingredient.extra_price

z2 = num2 + f2.start_price
print(z2)


# Общую стоимость заказа
print(z1 + z2)