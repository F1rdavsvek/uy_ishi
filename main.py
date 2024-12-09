# 1
import random
from decimal import Decimal, ROUND_DOWN
from datetime import datetime, timedelta

# class Temperature:
#     def __init__(self, value):
#         self.value = value
#         self.timestamp = self.generate_timestamp()
#     @property
#     def value(self):
#         return self._value
#     @value.setter
#     def value(self, val):
#         if not isinstance(val, (int, float)):
#             raise ValueError("Harorat raqam bo'lishi kerak!")
#         decimal_value = Decimal(val).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
#         if decimal_value < Decimal(-50) or decimal_value > Decimal(50):
#             raise ValueError("Harorat me’yordan chiqib ketdi!")
#         self._value = decimal_value
#     @staticmethod
#     def generate_timestamp():
#         return datetime.now() - timedelta(days=random.randint(0, 30))
#     def __str__(self):
#         return f"Harorat: {self.value}°C ({self.timestamp.strftime('%Y-%m-%d')})"
# temp = Temperature(random.uniform(-10, 40))
# print(temp)

# 2
# from decimal import Decimal
#
# class InsufficientFundsError(Exception):
#     pass
#
# class BankAccount:
#     def __init__(self, initial_balance):
#         self._balance = Decimal(initial_balance)
#
#     @property
#     def balance(self):
#         return self._balance
#
#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise InsufficientFundsError("Balans yetarli emas!")
#         self._balance = value
#
#     def deposit(self, amount):
#         self._balance += Decimal(amount)
#         print(f"Hisobingizga {amount} UZS qo'shildi. Joriy balans: {self.balance} UZS.")
#
#     def withdraw(self, amount):
#         if self._balance - Decimal(amount) < 0:
#             raise InsufficientFundsError("Balans yetarli emas!")
#         self._balance -= Decimal(amount)
#         print(f"{amount} UZS yechildi. Joriy balans: {self.balance} UZS.")
#
# account = BankAccount(500000)
#
# account.deposit(100000)
#
# try:
#     account.withdraw(500000)
# except InsufficientFundsError as e:
#     print(f"Xatolik: {e}")
#
# print(f"Joriy balans: {account.balance} UZS.")

# 3
# import random
# from decimal import Decimal
# from datetime import datetime, timedelta
#
# class Ticket:
#     def __init__(self, price):
#         self.price = price
#         self.sale_date = self.generate_sale_date()
#
#     @property
#     def price(self):
#         return self._price
#
#     @price.setter
#     def price(self, value):
#         if not isinstance(value, (int, float)):
#             raise ValueError("Chipta narxi Decimal formatda bo'lishi kerak!")
#         self._price = Decimal(value).quantize(Decimal('0.00'))
#
#     @staticmethod
#     def generate_sale_date():
#         return datetime.now() + timedelta(days=random.randint(0, 30))
#
#     def __str__(self):
#         return f"Chipta narxi: {self.price} UZS. Sotish sanasi: {self.sale_date.strftime('%Y-%m-%d')}."
#
# ticket = Ticket(random.uniform(100000, 200000))
# print(ticket)

# 4
# import random
# from decimal import Decimal
# from datetime import datetime, timedelta
#
# class EmployeeSalary:
#     def __init__(self, salary):
#         self.salary = salary
#         self.payment_date = self.generate_payment_date()
#
#     @property
#     def salary(self):
#         return self._salary
#
#     @salary.setter
#     def salary(self, value):
#         if not isinstance(value, (int, float)):
#             raise ValueError("Oylik maosh Decimal formatda bo'lishi kerak!")
#         self._salary = Decimal(value).quantize(Decimal('0.00'))
#
#     @staticmethod
#     def generate_payment_date():
#         return datetime.now() + timedelta(days=random.randint(1, 30))
#
#     def __str__(self):
#         return f"Ishchi oyligi: {self.salary} UZS. To‘lov sanasi: {self.payment_date.strftime('%Y-%m-%d')}."
#
# salary = EmployeeSalary(random.uniform(3000000, 5000000))
# print(salary)