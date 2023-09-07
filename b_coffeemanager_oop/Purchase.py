from Account import *

class Purchase:
    def __init__(self, coffee, purchase_cnt):
        self.__coffee = coffee
        self.__purchase_cnt = purchase_cnt
        self.__budget = coffee.get_cost() * purchase_cnt    # 필요 예산
        
    def execute(self, account):  # 매입에 필요한 금액을 지출로 등록하고 지출등록에 성공하면, 커피에게 성공했음을 리턴
        # account = Account() // Account를 생성해서 쓰는 것이 아니라 이미 menu에서 생성된, 매개변수로 받아온 account를 찾아옴
        
        if account.register_expenses(self.__budget):    # 지출 등록
            self.__coffee.add_stock(self.__purchase_cnt)    # 커피에게 매입수량만큼 재고 추가하라고 알림
            return True
        return False