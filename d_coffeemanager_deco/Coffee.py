from Purchase import *

class Coffee:
    def __init__(self, name, stock, total_sales_cnt, safety_stock, cost, price):
        self._name = name   # __name (private) => _name으로 변경
        self._stock = stock
        self._total_sales_cnt = total_sales_cnt
        self._safety_stock = safety_stock
        self._cost = cost
        self._price = price
        
    def offer(self, order_cnt): # 글처럼 읽히는 코드가 좋은 코드다..
        self.__deduct_stock(order_cnt)   # 재고 차감
        self.__add_total_sales_cnt(order_cnt) # 판매량 추가 // 문장 전체 드래그 -> ctrl + shift + R -> 메소드 추가하면 됨.
        
        if self._stock < self._safety_stock:
            # 안전재고 확보
            self.__add_safety_stock() 

    def __add_safety_stock(self):
        print('[system:log] 재고가 부족해 안전재고를 확보합니다.')
        purchase = Purchase(self, self.__safety_stock * 2)
            
        if purchase.execute():
            print('[system:log] 안전재고 확보에 성공했습니다.')
        else:
            print('[system:log] 안전재고 확보에 실패했습니다.')

    def __add_total_sales_cnt(self, order_cnt):
        self._total_sales_cnt += order_cnt   
    
    def __deduct_stock(self, order_cnt):
        self._stock -= order_cnt
    
    def add_stock(self, cnt):
        self._stock += cnt
    
    
    def get_name(self):
        return self._name

    def get_stock(self):
        return self._stock

    def get_total_sales_cnt(self):
        return self._total_sales_cnt

    def get_safety_stock(self):
        return self._safety_stock

    def get_cost(self):
        return self._cost

    def get_price(self):
        return self._price

    def __str__(self):
        return (
            "Coffee [name="
            + self.__name
            + ", stock="
            + str(self.__stock)
            + ", totalSalesCnt="
            + str(self.__total_sales_cnt)
            + ", safetyStock="
            + str(self.__safety_stock)
            + ", cost="
            + str(self.__cost)
            + ", price="
            + str(self.__price)
            + "]"
        )