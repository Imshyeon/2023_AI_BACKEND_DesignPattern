from Account import *

class Payment:
    def __init__(self, order):  # 메뉴에서 해당 주문에 대한 Order를 받아옴
        self.__order = order
        self.__pay_price = order.get_order_price()
        
        
    def execute(self,account):
        # account = Account() # Account는 한번 생성했으면 끝날때까지 계속해서 재사용해야함.
        account.register_sales(self.__pay_price)    # 결제 금액에 대한 매출 등록
        # print(account.get_balance()) 변경됨을 확인
        
    def get_order(self):
        return self.__order

    def set_order(self, order):
        self.__order = order

    def get_pay_price(self):
        return self.__pay_price

    def set_pay_price(self, pay_price):
        self.__pay_price = pay_price
        