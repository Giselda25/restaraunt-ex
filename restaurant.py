from abc import ABC, abstractmethod


# 1. АБСТРАКЦИЯ
class MenuItem(ABC):

  def __init__(self, name, price):
    self.name = name
    self.price = price

  @abstractmethod
  def calculate_price(self):
    pass


# ПОЛИМОРФИЗМ (Блюда)
class Pizza(MenuItem):

  def __init__(self, name, price, big=False):
    super().__init__(name, price)
    self.big = big

  def calculate_price(self):
    return self.price * 1.3 if self.big else self.price


class Drink(MenuItem):

  def calculate_price(self):
    return self.price


# 2. ИНКАПСУЛЯЦИЯ (Заказ)
class Order:

  def __init__(self):
    self.__items = []
    self.__status = "Создан"

  @property
  def status(self):
    return self.__status

  def next_step(self):
    statuses = ["Создан", "Готовится", "Доставляется", "Завершен"]
    curr = statuses.index(self.__status)
    if curr < len(statuses) - 1:
      self.__status = statuses[curr + 1]
      print(f"Статус: {self.__status}")

  def add_item(self, item):
    if self.__status != "Создан":
      print("Нельзя добавить: заказ уже готовится!")
      return
    self.__items.append(item)
    print(f"Добавлено: {item.name}")

  def get_total(self):
    return sum(item.calculate_price() for item in self.__items)

  def pay(self, payment):
    payment.pay(self.get_total())


# ПОЛИМОРФИЗМ (Оплата)
class CardPayment:

  def pay(self, amount):
    print(f"Оплата картой на сумму {amount} сом прошла успешно!")


class CashPayment:

  def pay(self, amount):
    print(f"Оплата наличными курьеру: {amount} сом.")


# ТЕСТ
if __name__ == "__main__":
  order = Order()
  order.add_item(Pizza("Пепперони", 600, big=True))
  order.add_item(Drink("Кола", 150))

  print(f"Итого: {order.get_total()} сом")

  order.next_step()
  order.add_item(Drink("Фанта", 140))  # Выдаст ошибку инкапсуляции

  order.pay(CardPayment())