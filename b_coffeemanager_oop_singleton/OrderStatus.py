from enum import Enum
# 연관된 상수들의 집합 = enum
# 다양한 주문이 취소되는 경우를 적어보자.

from Coffee import *

class OrderStatus(Enum):
    #OK = OrderStatus(0,'주문 생성 성공') 과 같은 의미.
    OK = (0, '주문 생성 성공')
    FAIL_CAUSE_SOLDOUT = (1, '품절로 인한 주문 실패')
    FAIL_CAUSE_STOCK = (2, '재고 부족으로 인한 주문 실패')
    COMPLITE = (3, '주문 완료')
    
    def __init__(self, code, desc):
        self.code = code
        self.desc = desc
    
    def is_ok(self):
        return self == OrderStatus.OK   # 해당 상태라 OK이면, 진행하라.
    
    def is_complete(self):
        return self == OrderStatus.COMPLITE # 해당 상태가 COMPLETE면, 진행
    
    def is_fail(self):
        return self in [OrderStatus.FAIL_CAUSE_SOLDOUT, OrderStatus.FAIL_CAUSE_STOCK]   # 이 상태(fail)이면 True
    
    @staticmethod
    def check_order_status(order):
        coffee = order.get_coffee()
        order_cnt = order.get_order_cnt()
        if coffee.get_stock() < order_cnt:
            return OrderStatus.FAIL_CAUSE_STOCK
        else:
            return OrderStatus.OK
        
    
    