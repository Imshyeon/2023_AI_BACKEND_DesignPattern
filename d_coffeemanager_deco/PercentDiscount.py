from Order import *
from Account import *

class PercentDiscount:
    
    @staticmethod
    def cal_discount_order_price(order_price):    #결제 금액 기준으로 할인하는 메서드
        discount = 0    # 중복 할인 혹은 다른 할인들 추가 적용 시, 합을 해야하기 때문에..
    
        if order_price >= 10000:
            discount = int(order_price * 0.1)    # 할인 금액을 계산  
        return discount 