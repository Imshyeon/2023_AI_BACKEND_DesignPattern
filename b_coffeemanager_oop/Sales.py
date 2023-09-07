from Payment import *
from Order import *

class Sales:
    def take_order(self, order, account):
        order.execute(account) # 주문수행
        payment = Payment(order)
        payment.execute(account)
        return payment  # 결제정보 반환