from random import random
import random

class Account:
    def __init__(self, name, amount):
        self.deposit_count = 0

        self.name = name
        self.amount = amount
        self.bank = "신한은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + "-" + num2 + "-" + num3

    def deposit(self, amount):
        self.amount += amount
        print("입금: ", amount)
        print("잔고: ", self.amount)

        self.deposit_count += 1
        if self.deposit_count % 5 == 0:
            self.amount = (self.amount * 1.01)

    def withdraw(self, amount):
        if self.amount > amount:
            self.amount -= amount

        print("출금: ", amount)
        print("잔고: ", self.amount)

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", f"{self.amount:,}")

seyeon = Account("조세연", 10000)
seyeon.deposit(50000)
seyeon.deposit(32000)
seyeon.deposit(20000)
seyeon.deposit(1000)
seyeon.deposit(15000)
seyeon.withdraw(10000)
seyeon.display_info()

    
