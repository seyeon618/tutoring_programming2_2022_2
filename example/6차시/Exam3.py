class Money:
    def __init__(self):
        self.money = 10000

    def buy_something(self, price):
        if price > self.money:
            print('보유 금액이 부족합니다.')
        else:
            print('구매 완료, 남은 금액은 ', self.money, '원 입니다.')
            self.money -= price

    def save_money(self, money):
        self.money += money

    def print_my_moeny(self):
        print('현재 보유 현금은 ', self.money, '원 입니다.')

seyeon = Money()
seyeon.buy_something(5000)
seyeon.print_my_moeny()